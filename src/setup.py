from setuptools import setup
import setup_translate

pkg = 'SystemPlugins.VFDControl'
setup(name='enigma2-plugin-systemplugins-vfdcontrol',
       version='3.0',
       description='vfd controller',
       package_dir={pkg: 'VFDControl'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
