---
catalog: Zenodo
contact_point:
  email: carderne@worldbank.org
  id: attribution_contact
  name: Christopher Arderne
  url: https://www.worldbank.org/ext/en/home
creator:
  email: carderne@worldbank.org
  id: attribution_creator
  name: Christopher Arderne
  url: https://www.worldbank.org/ext/en/home
dataset_id: rdls_exp-nismod_glb_powerline
description: A first composite map of the global power grid using publicly available
  open data, generated through the gridfinder tool. This dataset includes high-voltage
  (HV, >70 kV) transmission networks, predicted medium-voltage (MV, 10-70 kV) distribution
  networks, and low-voltage (LV, <1 kV) infrastructure estimates. The data shows that
  97% of the global population lives within 10km of a MV line, with significant regional
  variations. The dataset was created using state-of-the-art algorithms in geospatial
  data analysis, including night-time light imagery filtering and least-cost routing
  algorithms following roads and known distribution lines.
details: 'This research presents the first composite map of the global power grid
  using publicly available open data. The methodology uses multiple filtering algorithms
  applied to VIIRS night-time light imagery to identify electrification targets, then
  connects these locations through a many-to-many variant of Dijkstra''s algorithm
  using OpenStreetMap road networks as a cost function. The validation was performed
  across 16 electricity networks from 14 countries representing all World Bank income
  groupings, achieving 75% predictive accuracy across an equal-area grid with 15km
  edge length. The dataset comprises approximately 6.6 million km of high-voltage
  transmission lines (from OpenStreetMap), 7 million km of predicted medium-voltage
  distribution lines, and 69 million km of estimated low-voltage infrastructure. Important
  limitation: this dataset does not attempt to replicate actual network configurations
  or precise structures needed for electrical modeling such as power flow modeling.'
exposure:
  category: infrastructure
  dimension: structure
  quantity_kind: length
  taxonomy: GED4ALL
extra_attributions:
- email: enquiries@eci.ox.ac.uk
  id: attribution_collaborator1
  name: Environmental Change Institute, University of Oxford
  role: collaborator
  url: https://www.eci.ox.ac.uk
- email: cee-enquiries@auckland.ac.nz
  id: attribution_collaborator2
  name: Department of Civil and Environmental Engineering, University of Auckland
  role: collaborator
  url: https://www.auckland.ac.nz/en/engineering/about-the-faculty/engineering/civil-and-environmental-engineering.html
- email: info.ivm@vu.nl
  id: attribution_collaborator3
  name: Institute for Environmental Studies (IVM), Vrije Universiteit Amsterdam
  role: collaborator
  url: https://vu.nl/en/about-vu/research-institutes/ivm
hazard: null
license: CC-BY-4.0
loss: null
project:
  name: Predictive mapping of the global power system
  url: https://gridfinder.org
publisher:
  email: info@zenodo.org
  id: attribution_publisher
  name: Zenodo
  url: https://zenodo.org/records/3628142
purpose: To provide a standardized global dataset of electricity transmission and
  distribution networks for electrification planning, power sector resilience assessment,
  climate change adaptation, and achieving Sustainable Development Goal 7 (SDG 7).
  The dataset enables improved efforts in electricity modelling and planning, assessment
  of social inequalities, estimation of exposure to natural hazards, and quantification
  of electricity infrastructure roll-out requirements.
resources:
- coordinate_system: EPSG:4326
  description: Vectorized predicted distribution and transmission line network. Contains
    both existing OpenStreetMap lines (tagged in 'source' column) and newly predicted
    medium-voltage lines. Represents approximately 6.6 million km of high-voltage
    transmission lines and 7 million km of predicted medium-voltage distribution lines.
  download_url: https://zenodo.org/records/3628142/files/grid.gpkg
  format: GeoPackage (gpkg)
  id: resource_1
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Global Grid Network (Vector)
- coordinate_system: EPSG:54009
  description: Raster of predicted low-voltage infrastructure in kilometres per cell.
    Estimated using population density, night-time lights, urban extents, and national
    statistics to calculate the density of LV infrastructure (<1 kV). Comprises approximately
    69 million km of estimated low-voltage infrastructure globally.
  download_url: https://zenodo.org/records/3628142/files/lv.tif
  format: GeoTIFF (tif)
  id: resource_2
  media_type: null
  spatial_resolution: 250
  temporal: null
  title: Low-Voltage Infrastructure (Raster)
- coordinate_system: EPSG:4326
  description: Binary raster showing locations predicted to be connected to the distribution
    grid. Created through filtering of VIIRS night-time lights imagery using the 70th
    percentile value over 12 months, with a threshold value of 0.1 applied after convolving
    a distance-weighted filter.
  download_url: https://zenodo.org/records/3628142/files/targets.tif
  format: GeoTIFF (tif)
  id: resource_3
  media_type: null
  spatial_resolution: 450
  temporal: null
  title: Electrification Targets (Raster)
risk_data_type:
- exposure
schema: rdl-03
slug: rdls_exp-nismod_glb_powerline
spatial:
  countries:
  - GLO
  scale: global
title: Predictive mapping of the global power system using open data
version: 1.1.1
vulnerability: null
---
