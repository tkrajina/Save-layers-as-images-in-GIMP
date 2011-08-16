#!/usr/bin/env python

import gimpfu as mod_gimpfu
import re as mod_re

def save_layers( image, layer, image_type, destination_dir, new_width, new_height ):
	if new_width:
		new_width = int( new_width )

	if new_height:
		new_height = int( new_height )

	for layer in image.layers:
		layer_name = layer.name

		if new_width or new_height:

			if new_width:
				width = new_width
			else:
				width = int( layer.width * 1.0 * new_height / layer.height )

			if new_height:
				height = new_height
			else:
				height = int( layer.height * 1.0 * new_widht / layer.width )

			layer.scale( width, height )

		file_name = mod_re.sub( '\W+', '_', layer_name ).lower()
		file_name = '%s/%s.%s' % ( destination_dir, file_name, image_type )

		mod_gimpfu.pdb.gimp_file_save( image, layer, file_name, file_name )

mod_gimpfu.register(
        "save_layers",
        "Save layers to files",
        "Save layers to files",
        "Tomo Krajina",
        "Tomo Krajina",
        "2011",
        "<Image>/_Xtns/_Save layers",
        "RGB*, GRAY*",
        [
                ( mod_gimpfu.PF_STRING, "image_type", "Image type", "png" ),
                ( mod_gimpfu.PF_STRING, "destination_dir", "Destination directory", "." ),
                ( mod_gimpfu.PF_STRING, "new_width", "Width (empty if no resize)", "" ),
                ( mod_gimpfu.PF_STRING, "new_height", "Height (empty if no resize)", "" ),
        ],
        [],
        save_layers )

mod_gimpfu.main()
