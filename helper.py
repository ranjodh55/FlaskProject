import cv2 as cv


def process_image(filename, operation):
    print(f"The operation is {operation} and the filename is {filename}")
    img = cv.imread(f"uploads/{filename}")

    match operation:
        case "cgray":
            output_dir = f"static/{filename}"
            img_processed = cv.cvtColor(img, cv.COLOR_BGRA2GRAY)
            cv.imwrite(output_dir, img_processed)
            return output_dir

        case "cpng":
            output_dir = f"static/{filename.split('.')[0]}.png"
            cv.imwrite(output_dir, img)
            return output_dir

        case "cwebp":
            output_dir = f"static/{filename.split('.')[0]}.webp"
            cv.imwrite(output_dir, img)
            return output_dir
        case "cjpg":

            output_dir = f"static/{filename.split('.')[0]}.jpg"
            cv.imwrite(output_dir, img)
            return output_dir
