const packager = require('electron-packager')
const rebuild = require('electron-rebuild').default

packager({
  dir: __dirname,
  afterCopy: [(buildPath, electronVersion, platform, arch, callback) => {
    rebuild({ buildPath, electronVersion, arch })
      .then(() => callback())
      .catch((error) => callback(error));
  }]
}).catch(err => console.error(err))
