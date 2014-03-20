Bumblebee
=========

Bumblebee is a Python (2.7) script that allows you to replace strings in any text file (.txt, .log, .xml, .json, etc) with any other strings you want.
It simply iterates over all files and folders from a given directory, making the configured replacements.

One great thing about Bumblebee is that it does not replace the string in your original files. Insted, it creates a new directory structure just like the original one, but with the strings replaced as you wanted. This new structure is going to be under an automatically created folder called *new*.

Another great feature of Bumblebee is that it allows you to filter the files by providing a simple filtering function with the name of the file as an input (plus any other globals you wish to define) that you can fill in with any logical condition.

Finally, Bumblebee is really (I mean, really) simple, so you can understand ir easily and make any change you want to suit your needs.

I hope you find *him* usefull!

Important configurations
--------------------------

1) First you need to setup the base dir. Bumblebee will replace all files inside this directory. You can set this directory on line 9, when is says:

```python
base_dir = "Some_folder"
```

2) Now you need to setup your transformations. You can write them inside the if block at line 18:

```python
if __filter__(filename):
    target_content = target_content.replace("bumblebee sucks", "bumblebee rules!")
```

You can put as many transformations as you wish. Keep this in mind: transformations will be applied in the same order that you wrote them. So put more specific transormations at the beginning, and the most generic at the end.

3) [Optional] You can add a filter by implementing new filtering functionality inside the function called *__filter__*.

```python
def __filter__(fname):
    # put your filtering logic here
    return  true_or_false_value
```
