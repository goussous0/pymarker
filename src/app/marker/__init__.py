import zipfile
from io import BytesIO
from os import makedirs, path, getcwd
from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color


def water_mark_docx(doc_folder, docx_file, wm_text):
    print (f"Location  {doc_folder}") 
    print (f"Document  {docx_file}")
    print (f"WaterMark {wm_text}")

    # media_path = f"{doc_folder}/media"
    # makedirs(media_path, exist_ok=True)

    old_fd = zipfile.ZipFile(f"{doc_folder}/{docx_file}", "r")
    new_fd = zipfile.ZipFile(f"{doc_folder}/{docx_file}", "a")

    for file in old_fd.filelist:
        if "media" in file.filename:
            print (file.filename)
            
            with Image(file=BytesIO(old_fd.open(file.filename).read())) as background:
                with Image(width=background.width, height=background.height, background=Color("transparent")) as img:
                    img.composite_channel('all_channels', background, 'over', 0, 0)


                    # Create the watermark image
                    with Drawing() as draw:
                        with Image(width=500, height=50, background=Color("transparent")) as wm_img:
                            draw.font_size = 30
                            draw.fill_opacity = 0.5
                            draw.fill_color = Color("white")
                            draw.text(10, 40, wm_text)
                            draw(wm_img)
                            wm_img.rotate(-45)
                            # Composite the watermark onto the main image
                            img.composite( wm_img, 0, 0)
                            for i in range(-400, background.width, 400):
                                for j in range(-200, background.height, 100):
                                    img.composite(wm_img, i, j)

                    # local_path = f"{doc_folder}/{'/'.join(file.filename.split('/')[:-1])}"
                    # img.save(filename=f"{local_path}/{file.filename.split('/')[-1]}")


                    new_fd.writestr(file.filename, img.make_blob(format=file.filename.split('.')[-1]))
                    print (file.filename, file.filename.split('.')[-1])
