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

- Extend natural cliff materials across distant terrain, with a layered canyon
  variant for the Colorado Plateau and satellite-derived color and distant shading.
- Add the **Distant cliff faces** toggle and unified **Cliff detail** quality
  presets. Detail changes use safe load-time LOD selection.
- Add the approved 4K canyon diffuse with aligned near-cliff normal, roughness,
  and subtle ambient-occlusion maps; retain broader normals on distant cliffs
  and reduce their horizontal scale on the extreme-distance tier.
- Improve tall near-cliff geometry by refining vertical samples before applying
  scanned relief, preventing folded columns, and protecting terrain clearance
  through LOD simplification. Preserve road-cut fitting in mixed tiles.
- Retain the terrain-matched arid/limestone materials and dense-mesh vertex-limit
  fixes from the previous cliff testing release.

The 4K maps use the approved generated source, resampled to 4096 square; PBR
channels are inferred from the diffuse. Broad grooves from the source terrain
can remain visible. Canyon coverage, transitions and performance need testing.

### What to test

- Grand Canyon coverage from a high viewpoint: **36.05725, -112.14650**. Compare
  near cliffs, distant faces and the horizon under different sun angles.
- Terrain-fitted natural cliffs and road cuts, with different materials and regional colors.
- Scattered cliff rocks, terrain transition decals, and near-vehicle cliff collision.
- Urban highway cuts backed by original terrain, including rounded bases and crests.
- **Cliff detail** presets and separate **Cliff faces**, **Distant cliff faces**,
  **Scattered cliff rocks**, and **Cliff transition decals** settings. Reload the
  level after changing distant faces for a consistent view across loaded tiles.

See the [testing guide](https://github.com/Austint30/BeamNG.Earth/blob/{commit}/docs/CLIFF_TESTING.md)
for California, Austin, and El Paso locations, performance comparisons, and regression scenarios.
El Paso reference: **31.87810, -106.49561**, Woodrow Bean Transmountain Drive / TX-375.
The cliff regression suite and packaged-server smoke tests run before publication.

Please [report issues in this fork](https://github.com/Austint30/BeamNG.Earth/issues)
with coordinates, screenshots, version `{version}`, hardware, and FPS/frame-time comparisons.
These testing builds check this fork for updates, rather than upstream development builds.

Source: [`{commit[:8]}`](https://github.com/Austint30/BeamNG.Earth/commit/{commit}).
""")
