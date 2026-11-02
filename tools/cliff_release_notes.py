"""Release notes for the fork's isolated cliff-rock testing channel."""
import sys

version, commit = sys.argv[1:]
print(f"""> [!WARNING]
> **Experimental cliff-rock development build.** This fork build is for testing;
> it is not an upstream beta release. Coverage and performance are still being refined.

Download and run the launcher for your system:

- **Windows:** `BeamNG.Earth-{version}.exe`
- **Linux:** `BeamNG.Earth-{version}-x86_64.AppImage` (make it executable first)
- **BeamMP server:** `BeamNG.Earth-BeamMP-Server-{version}.zip`

Steam must be running. The launcher installs the matching mod and starts the world
server and game. Select **Freeroam > BeamNG.Earth**. Restart both the server and game
when replacing an older testing build, and keep the simulation unpaused while tiles load.

### Changes in this build

- Fix oversized cliff triangles stretching across roads by splitting dense meshes
  within the renderer's vertex limit, preserving the complete cliff surface.
- Add detailed arid road-cut materials selected by desert/steppe climate, with
  matching geometry relief and regional terrain color. Other climates retain
  the limestone road-cut material.
- Soften arid normal shading, restore restrained red-brown mineral color, and
  balance natural cliff brightness and fine grain against nearby cuts and terrain.
- Add regression coverage for dense mesh splitting and mixed material families.

### What to test

- Terrain-fitted natural cliffs and road cuts, with different materials and regional colors.
- Scattered cliff rocks, terrain transition decals, and near-vehicle cliff collision.
- Urban highway cuts backed by original terrain, including rounded bases and crests.
- Separate **Cliff faces**, **Scattered cliff rocks**, and **Cliff transition decals**
  toggles in the existing BeamNG.Earth settings UI. No environment variable is required.

See the [testing guide](https://github.com/Austint30/BeamNG.Earth/blob/{commit}/docs/CLIFF_TESTING.md)
for California, Austin, and El Paso locations, performance comparisons, and regression scenarios.
El Paso reference: **31.87810, -106.49561**, Woodrow Bean Transmountain Drive / TX-375.
The cliff regression suite and packaged-server smoke tests run before publication.

Please [report issues in this fork](https://github.com/Austint30/BeamNG.Earth/issues)
with coordinates, screenshots, version `{version}`, hardware, and FPS/frame-time comparisons.
These testing builds check this fork for updates, rather than upstream development builds.

Source: [`{commit[:8]}`](https://github.com/Austint30/BeamNG.Earth/commit/{commit}).
""")
