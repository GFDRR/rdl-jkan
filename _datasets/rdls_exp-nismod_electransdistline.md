---
attributions:
- entity:
    affiliation: null
    email: enquiries@eci.ox.ac.uk
    name: Environmental Change Institute, University of Oxford
    url: https://www.eci.ox.ac.uk
  id: attribution_collaborator1
  role: collaborator
- entity:
    affiliation: null
    email: cee-enquiries@auckland.ac.nz
    name: Department of Civil and Environmental Engineering, University of Auckland
    url: https://www.auckland.ac.nz/en/engineering/about-the-faculty/engineering/civil-and-environmental-engineering.html
  id: attribution_collaborator2
  role: collaborator
- entity:
    affiliation: null
    email: info.ivm@vu.nl
    name: Institute for Environmental Studies (IVM), Vrije Universiteit Amsterdam
    url: https://vu.nl/en/about-vu/research-institutes/ivm
  id: attribution_collaborator3
  role: collaborator
catalog: Zenodo
contact_point:
  affiliation: null
  email: carderne@worldbank.org
  name: Christopher Arderne
  url: https://www.worldbank.org/ext/en/home
creator:
  affiliation: null
  email: carderne@worldbank.org
  name: Christopher Arderne
  url: https://www.worldbank.org/ext/en/home
dataset_id: rdls_exp-nismod_electransdistline
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
- asset_type:
    description: Electricity transmission network classified using the GEM GED4ALL
      schema, combining OpenStreetMap high-voltage lines with predicted medium-voltage
      lines from Arderne et al. (2020) gridfinder model.
    id: pwr-lin
    scheme: GED4ALL
    title: Infrastructure taxonomy
    uri: https://wiki.openstreetmap.org/wiki/GED4ALL
  category: infrastructure
  id: exposure_electricity_transmission
  metrics:
  - dimension: structure
    id: metric_transmission_length
    measurement:
      quantity_kind: length
      unit: kilometre
- asset_type:
    description: Electricity distribution network classified using the GEM GED4ALL
      schema, sourced from predicted medium-voltage lines (Arderne et al. 2020 gridfinder
      model).
    id: pwr-lin
    scheme: GED4ALL
    title: Infrastructure taxonomy
    uri: https://wiki.openstreetmap.org/wiki/GED4ALL
  category: infrastructure
  id: exposure_electricity_distribution
  metrics:
  - dimension: structure
    id: metric_distribution_length
    measurement:
      quantity_kind: length
      unit: kilometre
- asset_type:
    description: Predicted low-voltage electricity infrastructure classified using
      the GEM GED4ALL schema, estimated from population density, night-time lights,
      and urban extents (Arderne et al. 2020 gridfinder model).
    id: pwr-lin
    scheme: GED4ALL
    title: Infrastructure taxonomy
    uri: https://wiki.openstreetmap.org/wiki/GED4ALL
  category: infrastructure
  id: exposure_electricity_low_voltage
  metrics:
  - dimension: structure
    id: metric_low_voltage_length
    measurement:
      quantity_kind: length
      unit: kilometre
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Electricity transmission and distribution network derived using the
    gridfinder predictive mapping model (Arderne et al. 2020). OpenStreetMap electrical
    infrastructure was supplemented with access-estimator model outputs, which used
    VIIRS Day/Night Band nighttime lights, GHS-POP population grids, GHS Settlement
    Model, and World Bank electrification rates as inputs. NASA SRTM DEM and ESA CCI
    land cover were used as ancillary data. The network was post-processed and topologically
    corrected using snkit.
  sources:
  - id: source_1
    license: https://opendatacommons.org/licenses/odbl/1-0/
    name: OpenStreetMap
    risk_data_type: null
    type: dataset
    url: https://planet.openstreetmap.org
    used_in: exposure
  - id: source_2
    license: https://creativecommons.org/licenses/by/4.0/
    name: VIIRS Day/Night Band Nighttime Lights
    risk_data_type: null
    type: dataset
    url: https://ngdc.noaa.gov/eog/viirs/download_dnb_composites.html
    used_in: exposure
  - id: source_3
    license: https://creativecommons.org/licenses/by/4.0/
    name: GHS Population (GHS-POP)
    risk_data_type: null
    type: dataset
    url: https://ghsl.jrc.ec.europa.eu/ghs_pop2019.php
    used_in: exposure
  - id: source_4
    license: https://creativecommons.org/licenses/by/4.0/
    name: GHS Settlement Model (GHS-SMOD)
    risk_data_type: null
    type: dataset
    url: https://ghsl.jrc.ec.europa.eu/ghs_smod2019.php
    used_in: exposure
  - id: source_5
    license: https://creativecommons.org/publicdomain/zero/1.0/
    name: NASA SRTM Digital Elevation Model
    risk_data_type: null
    type: dataset
    url: http://srtm.csi.cgiar.org/srtmdata
    used_in: exposure
  - id: source_6
    license: https://creativecommons.org/licenses/by/4.0/
    name: World Bank Electrification Rates
    risk_data_type: null
    type: dataset
    url: https://data.worldbank.org/indicator/EG.ELC.ACCS.ZS
    used_in: exposure
  - id: source_7
    license: https://creativecommons.org/licenses/by/4.0/
    name: ESA CCI Land Cover
    risk_data_type: null
    type: dataset
    url: https://maps.elie.ucl.ac.be/CCI/viewer
    used_in: exposure
  - id: source_8
    license: https://opensource.org/licenses/MIT
    name: gridfinder
    risk_data_type: null
    type: model
    url: https://github.com/carderne/gridfinder
    used_in: exposure
  - id: source_9
    license: https://opensource.org/licenses/MIT
    name: access-estimator
    risk_data_type: null
    type: model
    url: https://github.com/carderne/access-estimator
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
project:
  name: Predictive mapping of the global power system
  url: https://gridfinder.org
publisher:
  affiliation: null
  email: info@zenodo.org
  name: Zenodo
  url: https://zenodo.org/records/3628142
purpose: To provide a standardized global dataset of electricity transmission and
  distribution networks for electrification planning, power sector resilience assessment,
  climate change adaptation, and achieving Sustainable Development Goal 7 (SDG 7).
  The dataset enables improved efforts in electricity modelling and planning, assessment
  of social inequalities, estimation of exposure to natural hazards, and quantification
  of electricity infrastructure roll-out requirements.
referenced_by:
- author_names:
  - Christopher Arderne
  - Claire Nicolas
  - Conrad Zorn
  - Elco E. Koks
  date_published: '2020-01-15'
  doi: https://doi.org/10.1038/s41597-019-0347-4
  id: reference_1
  name: Predictive mapping of the global power system using open data
  url: https://www.nature.com/articles/s41597-019-0347-4
resources:
- access_url: https://zenodo.org/records/3628142
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Vectorized predicted distribution and transmission line network. Contains
    both existing OpenStreetMap lines (tagged in 'source' column) and newly predicted
    medium-voltage lines. Represents approximately 6.6 million km of high-voltage
    transmission lines and 7 million km of predicted medium-voltage distribution lines.
  download_url: https://zenodo.org/records/3628142/files/grid.gpkg
  format: null
  id: resource_1
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: Individual transmission and distribution line segment level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Global Grid Network (Vector)
- access_url: https://zenodo.org/records/3628142
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:54009
  description: Raster of predicted low-voltage infrastructure in kilometres per cell.
    Estimated using population density, night-time lights, urban extents, and national
    statistics to calculate the density of LV infrastructure (<1 kV). Comprises approximately
    69 million km of estimated low-voltage infrastructure globally.
  download_url: https://zenodo.org/records/3628142/files/lv.tif
  format: null
  id: resource_2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 250
  temporal: null
  temporal_resolution: null
  title: Low-Voltage Infrastructure (Raster)
- access_url: https://zenodo.org/records/3628142
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Binary raster showing locations predicted to be connected to the distribution
    grid. Created through filtering of VIIRS night-time lights imagery using the 70th
    percentile value over 12 months, with a threshold value of 0.1 applied after convolving
    a distance-weighted filter.
  download_url: https://zenodo.org/records/3628142/files/targets.tif
  format: null
  id: resource_3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 450
  temporal: null
  temporal_resolution: null
  title: Electrification Targets (Raster)
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-nismod_electransdistline
spatial:
  bbox: null
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal: null
temporal_resolution: null
title: 'Data from: Predictive mapping of the global power system using open data'
version: 1.1.1
vulnerability: null
---
