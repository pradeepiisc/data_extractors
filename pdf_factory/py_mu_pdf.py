import fitz
import io
# from PIL import Image
from pdf_factory.pdf_processor import PdfProcessor
# from IPython.display import Image, display


class PyMuPdfParser(PdfProcessor):
    def __init__(self) -> None:
        super().__init__()
        pass

    def get_text(self, pdf_file_pointer, page_index):
        page = pdf_file_pointer[page_index]
        return page.get_text()
    

    def get_image_params(self, pdf_file_pointer, page_index):
        """
        get xref, image_bytes, image_ext for all the images in page_index page number
        """
        page = pdf_file_pointer[page_index]
        image_params = []
        image_list = page.get_images()
        
        # printing number of images found in this page
        if image_list:
            pass
            # print(
            #     f"[+] Found a total of {len(image_list)} images in page {page_index}")
        else:
            # print("[!] No images found on page", page_index)
            return image_params

        
        current_params = {}
        for image_index, img in enumerate(image_list, start=1):
            # get the XREF of the image
            xref = img[0]
            current_params['xref'] = xref
            # extract the image bytes
            base_image = pdf_file_pointer.extract_image(xref)
            current_params['image_bytes'] = base_image["image"]
            current_params['image_ext'] = base_image["ext"]
            image_params.append(current_params)
            # display(Image(data=image_bytes))
        #  Image Params is a list containing as many image recors as the number of images on the given page

        return image_params

    def get_page_content(self, file_loc, page_number=0):
        pdf_file = fitz.open(file_loc)
        total_pages = len(pdf_file) 
        
        if page_number > 0 and page_number < total_pages:
            image_params = self.get_image_params(pdf_file, page_number)
            for each_image in image_params:
                pass
                # display(Image(data=each_image['image_bytes']))
            return

        page_to_image_params = {}
        for page_index in range(total_pages):
            # get the page itself
            page_to_image_params[page_index] = self.get_image_params(pdf_file, page_index)
        return page_to_image_params

    def process_file(self, file_path):
        pdf_file = fitz.open(file_path)
        # iterate over PDF pages
        total_pages = len(pdf_file)
        # print(total_pages)
        for page_index in range(total_pages):
            page_text = self.get_text(pdf_file, page_index)
            page_images = self.get_image_params(pdf_file, page_index)

            self.data.add_record(text=page_text, image=page_images)

        return self.data.records

            
