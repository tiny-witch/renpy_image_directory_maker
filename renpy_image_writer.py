import glob
import os


def renpy_image_check(directory_dir):
    dir_search = glob.glob(str(directory_dir))
    if len(dir_search) < 1:
        f.write(str('# these files  contain no images'))
    else:
        for i in range(0, len(dir_search)):
            png_list = glob.glob(dir_search[i] + "*png")
            jpg_list = glob.glob(dir_search[i] + "*jpg")
            folder_name = str(os.path.split(os.path.dirname(dir_search[i]))[-1])
            if int(len(png_list) + len(jpg_list)) >= 1:
                png_folder = (folder_name if folder_name != "images" else " ")
                f.write(str("# these are images in " + dir_search[i]) + "\n")
                for x in range(0, len(png_list)):
                    f.write(str(
                        "image " + png_folder[0] + " " + os.path.splitext(os.path.basename(png_list[x]))[
                            0] + " = " + '"' + png_list[
                            x] + '"') + "\n")

                for y in range(0, len(jpg_list)):
                    jpg_folder = (folder_name if folder_name != "images" else " ")
                    f.write(str(
                        "image " + jpg_folder[0] + " = " + '"' + jpg_list[
                            y] + '"') + "\n")
                    # print(str(
                    #     "image " + jpg_folder[0] + " = " + '"' + jpg_list[
                    #         y] + '"') + "\n")


f = open("image_directory.rpy", "w")

f.write(str("#Thanks for using my script! find more at https://github.com/tiny-witch" + "\n"))
f.write(str("# This file will include jpg and png images only" + "\n"))
f.write(str("# Here are the directories this file searched for images:" + "\n"))
dir_list = ["*", "*/", "*/*/"]
for lst in range(0, len(dir_list)):
    temp_list = glob.glob(str(dir_list[lst]))
    # print("temp list is: ", temp_list)
    # print(temp_list[0])
    # print(len(temp_list))

    k = int(len(temp_list))
    # print(k)

    for r in range(0, k):
        # print(r)
        # f.write(str((" "*8)+"# " + str(temp_list[r]) + "\n"))
        if os.path.isdir(temp_list[r]):
            f.write(str("# " + (" " * 8) + ("-" * 8 * lst) + str(temp_list[r]) + "\n"))
            # f.write(str((" " * 8) + "# " + "is directory" + "\n"))
# print('\n'.join([str(glob.glob(str(dir_list[lst]))) for lst in range(0, len(dir_list))]))
for q in range(0, len(dir_list)):
    renpy_image_check(dir_list[q])

f.close()

if __name__ == "__main__":
    import os
    import glob

    f = open("image_directory.rpy", "w")

    f.write(str("# Thanks for using my script! find more at https://github.com/tiny-witch" + "\n"))
    f.write(str("# This file will include jpg and png images only" + "\n"))
    f.write(str("# Here are the directories this file searched for images:" + "\n"))
    dir_list = ["*", "*/", "*/*/"]
    for lst in range(0, len(dir_list)):
        temp_list = glob.glob(str(dir_list[lst]))
        # print("temp list is: ", temp_list)
        # print(temp_list[0])
        # print(len(temp_list))

        k = int(len(temp_list))
        # print(k)

        for r in range(0, k):
            # print(r)
            # f.write(str((" "*8)+"# " + str(temp_list[r]) + "\n"))
            if os.path.isdir(temp_list[r]):
                f.write(str("# " + (" " * 8) + ("-" * 8 * lst) + str(temp_list[r]) + "\n"))
                # f.write(str((" " * 8) + "# " + "is directory" + "\n"))
    # print('\n'.join([str(glob.glob(str(dir_list[lst]))) for lst in range(0, len(dir_list))]))
    for q in range(0, len(dir_list)):
        renpy_image_check(dir_list[q])

    f.close()

