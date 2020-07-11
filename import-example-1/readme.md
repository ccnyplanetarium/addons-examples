A sample asset that will load a speck file and place it in a scene.

Request is from your scene file by including:

asset.request('import-example-1/datapoints')

Assuming you've put this folder directly under the assets.

asset.request will look directly under the OpenSpace15.x/data/assets directory, so if you put it elsewhere, you will need to adjust the path in the above command.

a simple colormap is contained in the colors.cmap files

the speck file is 4 columns:

x y z colorkey
