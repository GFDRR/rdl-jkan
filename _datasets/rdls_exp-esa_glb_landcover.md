---
contact_point:
  email: Pierre.Defourny@uclouvain.be
  id: attribution_contact
  name: Pierre Defourny
  url: https://www.uclouvain.be/en/research-institutes/eli/research-team
creator:
  email: Pierre.Defourny@uclouvain.be
  id: attribution_creator
  name: UCL-Geomatics
  url: https://www.uclouvain.be/en/research-institutes/eli/elie/research-projects
dataset_id: rdls_exp-esa_glb_landcover
description: This dataset provides global land cover maps at 300m spatial resolution
  describing the land surface into 22 classes defined using the UN FAO Land Cover
  Classification System (LCCS). The maps cover the period from 1992 to present with
  annual temporal resolution. The dataset includes land cover classification maps
  along with four quality flags documenting the reliability of the classification
  and change detection processes. These maps are produced using a baseline classification
  approach applied to the MERIS Full and Reduced Resolution archive (2003-2012), which
  is then back-dated and updated using AVHRR (1992-1999), SPOT-VGT (1998-2012), PROBA-V
  (2013-2019), and Sentinel-3 OLCI/SLSTR (2020-present) time series. The maps for
  2016-2022 are consistent with the ESA CCI global annual land cover maps from 1992-2015,
  ensuring temporal continuity across the entire time series.
details: "The land cover maps are delivered in NetCDF-4 format following CF-1.6 conventions,\
  \ with a geographic coordinate system based on WGS84 using Plate Carr\xE9e projection.\
  \ Each annual map includes five bands: lccs_class (land cover classification), processed_flag\
  \ (processing status), current_pixel_state (pixel state during baseline generation),\
  \ observation_count (number of valid observations), and change_count (number of\
  \ detected land cover changes during 1992-2022). The change detection methodology\
  \ captures transitions between six IPCC land categories (cropland, forest, grassland,\
  \ wetland, settlement, and other land), with changes requiring confirmation over\
  \ at least two consecutive years. The dataset achieves an overall accuracy of approximately\
  \ 70% when validated against independent reference samples. Four land cover classes\
  \ rely on external datasets: tree cover flooded saline water (mangroves from global\
  \ atlas), urban areas (Global Human Settlement Layer and Global Urban Footprint),\
  \ water bodies (CCI global open water bodies map), and permanent snow and ice (Randolph\
  \ Glaciers Inventory). The spatial resolution corresponds to 0.002778\xB0 (approximately\
  \ 300m at the equator, ~200m in mid-latitudes). File sizes are approximately 2.5\
  \ GB per annual map with internal LZW compression."
exposure:
- category: natural_environment
  dimension: content
  quantity_kind: area
  taxonomy: GED4ALL
extra_attributions:
- email: info@brockmann-consult.de
  id: attribution_collaborator
  name: Brockmann Consult GmbH
  role: collaborator
  url: https://www.brockmann-consult.de/
hazard: null
license: CC-BY-4.0
loss: null
project:
  name: Climate Change Initiative - European Space Agency
  url: http://www.esa-landcover-cci.org/
publisher:
  email: copernicus-support@ecmwf.int
  id: attribution_publisher
  name: European Centre for Medium-Range Weather Forecasts (ECMWF) / Copernicus Climate
    Change Service (C3S)
  url: https://cds.climate.copernicus.eu/
purpose: This dataset is designed primarily to support climate modeling communities
  by providing long-term, temporally consistent land cover information as an Essential
  Climate Variable (ECV). The comprehensive legend spanning global-scale landscape
  diversity makes it valuable for various applications including climate modeling,
  land accounting, forest monitoring, desertification studies, and scientific research.
  The dataset addresses user requirements for global coverage, multi-decadal temporal
  extent with yearly updates, thematic detail compatible with Plant Functional Types
  (PFTs) used in climate models, and transparent quality assessment through independent
  validation.
resources:
- coordinate_system: EPSG:32662
  description: Land cover class per pixel, according to a legend of 22 classes, defined
    using the Land Cover Classification System developed by the United Nations Food
    and Agriculture Organization. Distinct values are encoded as unsigned byte (0..255).
    The complete legend is available in the NetCDF files metadata and in the Product
    User Guide documentation.
  download_url: https://cds.climate.copernicus.eu/datasets/satellite-land-cover?tab=overview
  format: NetCDF (nc)
  id: resource_TKupNUwN
  media_type: null
  spatial_resolution: 300
  temporal:
    duration: ''
    end: '2022-01-01'
    start: '1992-01-01'
    temporal_resolution: P1Y
  title: Land cover class
- coordinate_system: EPSG:32662
  description: Number of years where land cover class changes have occurred, since
    1992. 0 for stable, greater than 0 for changes.
  download_url: https://cds.climate.copernicus.eu/datasets/satellite-land-cover?tab=overview
  format: NetCDF (nc)
  id: resource_zBYXaj1X
  media_type: null
  spatial_resolution: 300
  temporal:
    duration: ''
    end: '2022-01-01'
    start: '1992-01-01'
    temporal_resolution: P1Y
  title: Change count
- coordinate_system: EPSG:32662
  description: 'Pixel identification from satellite surface reflectance observations,
    mainly distinguishing between land, water, and snow/ice. Six values are used:
    1, 2, 3, 4, 5, 6; respectively meaning: clear land, clear water, clear snow ice,
    cloud, cloud shadow, filled.'
  download_url: https://cds.climate.copernicus.eu/datasets/satellite-land-cover?tab=overview
  format: NetCDF (nc)
  id: resource_cNqN7bjT
  media_type: null
  spatial_resolution: 300
  temporal:
    duration: ''
    end: '2022-01-01'
    start: '1992-01-01'
    temporal_resolution: P1Y
  title: Current pixel state
- coordinate_system: EPSG:32662
  description: 'Flag to mark areas that could not be classified. Two values are used:
    0, 1; respectively meaning: not_processed, processed.'
  download_url: https://cds.climate.copernicus.eu/datasets/satellite-land-cover?tab=overview
  format: NetCDF (nc)
  id: resource_ElzHcgz1
  media_type: null
  spatial_resolution: 300
  temporal:
    duration: ''
    end: '2022-01-01'
    start: '1992-01-01'
    temporal_resolution: P1Y
  title: Processed flag
- coordinate_system: EPSG:32662
  description: Number of valid satellite observations that have contributed to each
    pixel's classification
  download_url: https://cds.climate.copernicus.eu/datasets/satellite-land-cover?tab=overview
  format: NetCDF (nc)
  id: resource_3kGbDusD
  media_type: null
  spatial_resolution: 300
  temporal:
    duration: ''
    end: '2022-01-01'
    start: '1992-01-01'
    temporal_resolution: P1Y
  title: Observation count
risk_data_type:
- exposure
schema: rdl-03
slug: rdls_exp-esa_glb_landcover
spatial:
  bbox:
  - -180
  - -90
  - 180
  - 90
  centroid:
  - 0
  - 0
  countries:
  - GLO
  geometry:
    type: ''
  scale: global
title: Land cover classification gridded maps from 1992 to present derived from satellite
  observations
version: 2.1.1
vulnerability: null
---
