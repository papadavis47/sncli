
# Copyright (c) 2014 Eric Davis
# Licensed under the MIT License

import os, json, tempfile

def tempfile_create(note, raw=False):
    if raw:
        # dump the raw json of the note
        tf = tempfile.NamedTemporaryFile(suffix='.json', delete=False)
        json.dump(note, tf, indent=2)
        tf.flush()
    else:
        ext = '.txt'
        if note and \
           'systemtags' in note and \
           'markdown' in note['systemtags']:
            ext = '.mkd'
        tf = tempfile.NamedTemporaryFile(suffix=ext, delete=False)
        if note:
            contents = note['content']
            tf.write(encode_utf_8(contents))
        tf.flush()
    return tf

def encode_utf_8(string):
    # This code also exists in sncli.py. Move into an encoding or utility class if other areas need encoding.
    return string.encode("utf-8") if isinstance(string, str) else string

def tempfile_delete(tf):
    if tf:
        os.unlink(tf.name)

def tempfile_name(tf):
    if tf:
        return tf.name
    return ''

def tempfile_content(tf):
    # This seems like a hack. When editing with Gedit, tf file contents weren't getting 
    # updated in memory, even though it successfully saved on disk.
    updated_tf_contents = open(tf.name, 'r').read()
    tf.write(updated_tf_contents.encode("utf-8"))
    return updated_tf_contents
