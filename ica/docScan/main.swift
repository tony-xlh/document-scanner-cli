//
//  main.swift
//  docScan
//
//  Created by xulihang on 2025/7/28.
//

import Foundation
import ImageCaptureCore
import AppKit


class ScannerManager: NSObject, ICDeviceBrowserDelegate {
    private var deviceBrowser: ICDeviceBrowser!
    private var scanners: [ICScannerDevice] = []
    private var currentScanner: ICScannerDevice?
    private var scanCompletionHandler: ((Result<URL, Error>) -> Void)?
    
    override init() {
        super.init()
        setupDeviceBrowser()
    }
    
    private func setupDeviceBrowser() {
        deviceBrowser = ICDeviceBrowser()
        deviceBrowser.delegate = self
        let mask = ICDeviceTypeMask(rawValue:
                    ICDeviceTypeMask.scanner.rawValue |
                    ICDeviceLocationTypeMask.local.rawValue |
                    ICDeviceLocationTypeMask.bonjour.rawValue |
                    ICDeviceLocationTypeMask.shared.rawValue)
        deviceBrowser.browsedDeviceTypeMask = mask!
        deviceBrowser.start()
    }
    
    func listScanners(completion: @escaping ([ICScannerDevice]) -> Void) {
        DispatchQueue.main.asyncAfter(deadline: .now() + 1) {
            completion(self.scanners)
        }
    }
    
    // MARK: - ICDeviceBrowserDelegate
    
    func deviceBrowser(_ browser: ICDeviceBrowser, didAdd device: ICDevice, moreComing: Bool) {
        guard let scanner = device as? ICScannerDevice else { return }
        scanners.append(scanner)
    }
    
    func deviceBrowser(_ browser: ICDeviceBrowser, didRemove device: ICDevice, moreGoing: Bool) {
        if let index = scanners.firstIndex(where: { $0 == device }) {
            scanners.remove(at: index)
        }
    }
}

func main() {
    let scannerManager = ScannerManager()
    print("Finding scanners...")
    scannerManager.listScanners { scanners in
        if scanners.isEmpty {
            print("No scanners found.")
            return
        }
        print(scanners)
    }
    RunLoop.current.run()
}

main()
