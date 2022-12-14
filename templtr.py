import os
import shutil

base_template = "BaseTemplate"
templates_dir = "src/templates"


class Templatr():
    def __init__(self):
        pass

    # Get the option selected by the user
    def get_users_selected_option(self, options):
        for idx, element in enumerate(options):
            print("{}) {}".format(idx + 1, element))

        i = input("Please choose a template option: ")
        try:
            if 0 < int(i) <= len(options):
                return int(i) - 1
        except:
            pass
        return None

    # Gets the template options
    def get_template_options(self):
        list_of_templates = os.listdir(templates_dir)
        template_options = []

        for template in list_of_templates:
            dir = f"{templates_dir}/{template}"

            if os.path.isdir(dir):
                template_options.append(template)

        return template_options

    # Get file names in the directory
    # Open and rename anything with BaseTemplate
    # Rename the folders
    def rename_copied_files(self, dst_dir, name_of_files_and_folders):
        list_of_files = os.listdir(dst_dir)

        try:
            for file in list_of_files:
                old_name = f"{dst_dir}{file}"
                new_name = f"{dst_dir}{file.replace(base_template, name_of_files_and_folders)}"

                # Let's rename the contents of our files
                with open(old_name, "r") as f:
                    data = f.read()

                    # Searching and replacing the text
                    # using the replace() function
                    data = data.replace(
                        base_template, name_of_files_and_folders)

                with open(old_name, 'w') as f:

                    # Writing the replaced data in our
                    # text file
                    f.write(data)
                # Finally rename the base folder
                os.rename(old_name, new_name)

            # And show a success message
            print(f"\nTemplate {name_of_files_and_folders} was successfully created at {dst_dir[:-1]}")

        except:
            print("There was an error renaming the folder(s) and or file(s)")

    # Creates a directory and a list of files based off
    # a users selected template
    def create_template(self):
        print("Welcome to Templtr\n")

        dir_to_place_template = input(
            "Where do you want to place the template? ")

        dst_dir = None
        name_of_files_and_folders = input(
            "What would you like to name the template directory and files? ")

        # Check if the directory exists
        while True:
            dst_dir = f"{dir_to_place_template}/{name_of_files_and_folders}/"

            if (os.path.exists(dst_dir)):
                name_of_files_and_folders = input(
                    f"{name_of_files_and_folders} directory already exists. Please choose a different name: ")
                continue

            break

        template_options = self.get_template_options()
        selected_index = self.get_users_selected_option(template_options)
        selected_template = template_options[selected_index]

        # Get the template to copy
        src_dir = f"{templates_dir}/{selected_template}"

        # Copy the template files to the user selected directory
        shutil.copytree(src_dir, dst_dir)

        # Rename the copied files to match the user created name
        self.rename_copied_files(dst_dir, name_of_files_and_folders)


def main():
    templatr = Templatr()
    templatr.create_template()


if __name__ == "__main__":
    main()
