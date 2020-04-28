# boilerplate-gen
Boilerplate generation tool for various tech stacks

# Setting up
This need python3 installed, if possible python3.8

Make sure you've installed `pipenv`

## On Mac
`$ brew install pipenv` if you have brew

`$ pip3 install pipenv` if you do not have brew but have pip3

## On linux

If you have pip installed

`$ pip3 install pipenv`

If you do not have pip installed

### Ubuntu 17.10

```
$ sudo apt install software-properties-common python-software-properties
$ sudo add-apt-repository ppa:pypa/ppa
$ sudo apt update
$ sudo apt install pipenv
```

### Fedora 28

`$ sudo dnf install pipenv`

### Generic

`$ curl https://raw.githubusercontent.com/pypa/pipenv/master/get-pipenv.py | python`


# Using

Clone the repo and go to the repo root, and run

`$ pipenv shell` to go the virtual environment, and then

`$ pipenv install` to install the requirements, and then

`$ python -m boilerplate_gen` to see the usage guide 



# Help

Help is on the tool itself

`$ python -m boilerplate_gen --help` for all help

`$ python -m boilerplate_gen generate --help` for help regarding the generate command

`$ python -m boilerplate_gen list --help` for help regarding the list command

`$ python -m boilerplate_gen info --help` for help regarding the info command


# Configuration

By default, it assumes the configuration files are in `~/.py-boilerplate-gen/` directory

User specific configuration file is looked first, if it is present on `~/.py-boilerplate-gen/config.cfg`

If not, the default configuration file supplied with the package/module is applied. 

The default configuration file looks like the following

```
[config]
boilerplates_dir=~/.py-boilerplate-gen/boilerplates
```

# Boilerplates

This generater comes pre-packaged with some core boilerplates that are commonly used, which you can query using the list command as described above.

Besides that, you can also write your own boilerplates, and put it on the `boilerplates_dir` which is `~/.py-boilerplate-gen/boilerplates` by default, but you are able to change it


# Writing your own boilerplate

The boilerplate is nothing but a configuration file, and a directory structure that will be copied as part of the generation process

## Steps:

### Step 1
Create a directory where you'll write your boilerplate

### Step 2

Add a file named `config.cfg` inside that directory

Sample contents of `config.cfg` are listed below

```
;=========================
; Boilerplate information
;=========================
[boilerplate]
; Name of script (should be executable) to run before files are copied if you wish to
; It is run on the context of plugin directory (always relative path)
; If you don't wish to runa script before files are copied, leave this empty
before_copy=before_copy.py

; Name of script (should be executable) to run after files are copied
; It is run on the context of plugin directory (always relative path)
; You could do cleanup for all the dirty works that before_copy introduced
; on this script
; If you don't wish to run a script on boilerplate directory after files are copied, leave this empty
after_copy=after_copy.py

; Name of script (should be executable) to run after files are copied
; and the after_copy script is run. This is run on the context of the user
; directory (i.e., the place where user is installing the boilerplate)
; If you don't wish to run a script on user directory after files are copied, leave this empty
during_install=during_install.py

; Where to copy files from, after running the script, always relative path
; This is required. A boilerplate always has some things to copy over
; But if you absolutely don't need anything, just make sure the folder defined here has nothing in it
file_path=files

; You can choose to install this boilerplate after some other boilerplate(s), comma separated.
; Not supported yet
install_after_boilerplate=

; =================================================================
; If you want to ask user for any variables, put the names below,
; when running your script it will add a prefix
; PYTHON_BOILERPLATE_GEN_USERVAR_<VARNAME>
; and make it available to all of your scripts
; Format:
; var_name=<required/optional>,[optional_default_value]
; You can skip the whole section if you don't require any user input
; or if you plan on getting the user input via your scripts
; =================================================================
[user_vars]
app_name=required
app_version=optional,1.0.0
app_main=optional,index.js
app_desc=optional,Sample App
repo_url=optional
keywords=optional
author=optional
bug_url=optional
homepage=optional



;========================================
; Add if you depend on particular stacks
; Note: This is not validated at the moment
;========================================
[depends_on]
; What languages/os packages needs to be installed, comma separated,
; Currently supported: nodejs
; Sensible defaults for the packages are below
stacks=nodejs

;==================================================
; Nodejs configuration
; Note: This is not validated at the moment
;==================================================
[stacks.nodejs]
; Version of nodejs that is required on the system
version=v12.6.0

; If strict version is true then system needs to have that version
; otherwise, it's ignored as long as the stack exists
; default : false
strict_version=false 
```

### Step 3 
Add your files on the proper directory inside your boilerplate dir.

And if you require to, write the `before_copy`, `after_copy` and/or `during_install` scripts


# Example

The core boilerplate for a reactjs repository with rxjs and typescript can be thought as an example

It has a bunch of files that we know needs to be copied, but it misses package.json. So we utilize the user_data section on the config
to get some information about the app that we're going to bootstrap and create a skeleton package.json . We save that file to
the folder which is going to get copied over.

After the folder is copied, we need to make sure that we revert our folder to the original state, and thus we delete te package.json from the boilerplate folder

After that's done, we install latest versions of the packages required using npm. 



