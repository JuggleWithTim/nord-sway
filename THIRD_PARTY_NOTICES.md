# Artwork and dependencies

The original Nord interface artwork in `assets/icons/`, `assets/buttons/`,
`assets/Nordweb_bg.png`, and `assets/nord-logo.png` was supplied through the
NordRevived web client. The wallpaper SVG/PNG and screenshots also incorporate
that artwork. Those assets and marks remain the property of their respective
rights holders; the repository's MIT license does not relicense them.

The `*_middle_wide.png` files repeat the original one-pixel button center
without changing its colors. This avoids GTK's transparent-edge filtering.

DIN-Medium and Verdana fonts are **not distributed** here. The installer can
import them from an existing local NordWebClient checkout, or use an installed
fallback font.

Papirus icons are **not distributed** here. When Papirus is already installed,
the installer builds the orange folder overlay from those local files. Papirus
is maintained at https://github.com/PapirusDevelopmentTeam/papirus-icon-theme
under GPL-3.0; its original license and attribution continue to apply to those
locally copied icons.

Sway, Waybar, Wofi, Foot, Mako, Grim, GTK and their dependencies are installed
separately and retain their own licenses.
