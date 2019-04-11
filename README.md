# Minecraft Plugin Manager

MPM is an utility designed to ease the installation of a Minecraft server with or without plugins.

## Commands

### python mpm.py init \<type\> \[version\]

Type : Can be one of "vanilla" or "spongevanilla". The first will fetch the Mojang versions of the game whereas the 
second one use Sponge vanilla ones.  
Version : The version can be set to force a specific version. By default, it will download the latest/recommended one.  
Ex : ```python mpm.py init vanilla```

### python mpm.py install \<plugin\>

The plugin must be a direct URL, for now.
It will create a mods folder if needed and put the newly downloaded mod inside it.  
Ex : ```python mpm.py install https://github.com/OnapleRPG/Itemizer/releases/download/1.5.4/Itemizer-1.5.4.jar```

## More to come ?

Feel free to express your interest, as I will surely add more features if some people use it. If it doesn't happen... 
probably not much. You can see some of the planned features among the Github issues.
