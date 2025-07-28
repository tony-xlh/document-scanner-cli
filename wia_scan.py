import os
from PIL import Image
import pythoncom
from win32com.client import Dispatch

def list_scanners():
    manager = Dispatch("WIA.DeviceManager")
    devices = manager.DeviceInfos
    for i in range(1, devices.Count + 1):
        device = devices.Item(i)
        # Check if the device is a scanner (Type = 1)
        if device.Type == 1:
            print(f"  Name: {device.Properties['Name'].Value}")
            print(f"  ID: {device.DeviceID}")
            print(f"  Description: {device.Properties['Description'].Value}")
            print("  ----------------")
    return devices
    

def scan_document(output_folder="scanned_documents",scanner_name=""):
    """
    Scan a document using WIA interface and save as image file
    
    Parameters:
        output_folder: Path to save scanned documents
    """
    # Create WIA objects
    wia = Dispatch("WIA.CommonDialog")

    selected_device = None
    if scanner_name != "":
        devices = list_scanners()
        for i in range(1, devices.Count + 1):
            device = devices.Item(i)
            # Check if the device is a scanner (Type = 1)
            if device.Type == 1:
                if device.Properties['Name'].Value == scanner_name:
                    selected_device = device.Connect()
                    break
    # Execute the scan
    print("Scanning...")
    
    img = None
    if selected_device is None:
        img = wia.ShowAcquireImage()  # Show scanning dialog
    else:

        img = wia.ShowTransfer(selected_device.Items[1])  # Transfer the scanned image
        
    if img is None:
        print("Scanning failed")
        return
    
    # Create output directory if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # Generate unique filename with timestamp
    import time
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    output_format = "PNG"
    output_path = os.path.join(output_folder, f"scan_{timestamp}.{output_format.lower()}")
    
    # Save the image
    if hasattr(img, "SaveFile"):  # WIA 2.0 compatible method
        img.SaveFile(output_path)
    else:  # Fallback for WIA 1.0 using PIL
        pil_img = Image.fromarray(img)
        pil_img.save(output_path)
    
    print(f"Scan completed. File saved to: {output_path}")
    return output_path

if __name__ == "__main__":
    # Example usage
    scan_document(output_folder="my_scans",scanner_name="")
    