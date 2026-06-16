---
attributions:
- entity:
    affiliation: null
    email: info@brockmann-consult.de
    name: Brockmann Consult GmbH
    url: https://www.brockmann-consult.de/
  id: attribution_collaborator
  role: collaborator
catalog: Copernicus Climate Data Store
contact_point:
  affiliation: null
  email: Pierre.Defourny@uclouvain.be
  name: Pierre Defourny
  url: https://www.uclouvain.be/en/research-institutes/eli/research-team
creator:
  affiliation: null
  email: Pierre.Defourny@uclouvain.be
  name: UCL-Geomatics
  url: https://www.uclouvain.be/en/research-institutes/eli/elie/research-projects
dataset_id: rdls_exp-esacci_landcover
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
- asset_type:
    description: null
    id: land_cover
    scheme: null
    title: Land cover taxonomy
    uri: null
  category: natural_environment
  id: exp_metrics_1
  metrics:
  - dimension: content
    id: metric_ZOZhoIGn
    measurement:
      quantity_kind: area
      unit: null
  - dimension: content
    id: metric_VsifqcGY
    measurement:
      quantity_kind: area
      unit: null
  - dimension: content
    id: metric_RFddQRNI
    measurement:
      quantity_kind: area
      unit: null
  - dimension: content
    id: metric_scwiw8Y2
    measurement:
      quantity_kind: area
      unit: null
  - dimension: content
    id: metric_du9FyKrw
    measurement:
      quantity_kind: area
      unit: null
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Global land cover classification produced by the ESA Climate Change
    Initiative Land Cover (CCI-LC) project from Copernicus Sentinel-3 OLCI satellite
    imagery at 300 m spatial resolution. Annual land cover maps were generated using
    an unsupervised classification approach; the 2020 reference year product was used.
  sources:
  - id: source_WFhKRWnY
    license: https://creativecommons.org/licenses/by/4.0/
    name: Copernicus Sentinel-3 Ocean and Land Colour Instrument (OLCI)
    risk_data_type: null
    type: dataset
    url: https://dataspace.copernicus.eu/explore-data/data-collections/sentinel-data/sentinel-3
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
project:
  name: Climate Change Initiative - European Space Agency
  url: http://www.esa-landcover-cci.org/
publisher:
  affiliation: null
  email: copernicus-support@ecmwf.int
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
referenced_by: []
resources:
- access_url: https://cds.climate.copernicus.eu/datasets/satellite-land-cover?tab=overview
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:32662
  description: Land cover class per pixel, according to a legend of 22 classes, defined
    using the Land Cover Classification System developed by the United Nations Food
    and Agriculture Organization. Distinct values are encoded as unsigned byte (0..255).
    The complete legend is available in the NetCDF files metadata and in the Product
    User Guide documentation.
  download_url: null
  format: null
  id: resource_TKupNUwN
  media_type: application/netcdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 300
  temporal:
    central_year: null
    duration: null
    end: '2022-01-01'
    start: '1992-01-01'
  temporal_resolution: P1Y
  title: Land cover class
- access_url: https://cds.climate.copernicus.eu/datasets/satellite-land-cover?tab=overview
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:32662
  description: Number of years where land cover class changes have occurred, since
    1992. 0 for stable, greater than 0 for changes.
  download_url: null
  format: null
  id: resource_zBYXaj1X
  media_type: application/netcdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 300
  temporal:
    central_year: null
    duration: null
    end: '2022-01-01'
    start: '1992-01-01'
  temporal_resolution: P1Y
  title: Change count
- access_url: https://cds.climate.copernicus.eu/datasets/satellite-land-cover?tab=overview
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:32662
  description: 'Pixel identification from satellite surface reflectance observations,
    mainly distinguishing between land, water, and snow/ice. Six values are used:
    1, 2, 3, 4, 5, 6; respectively meaning: clear land, clear water, clear snow ice,
    cloud, cloud shadow, filled.'
  download_url: null
  format: null
  id: resource_cNqN7bjT
  media_type: application/netcdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 300
  temporal:
    central_year: null
    duration: null
    end: '2022-01-01'
    start: '1992-01-01'
  temporal_resolution: P1Y
  title: Current pixel state
- access_url: https://cds.climate.copernicus.eu/datasets/satellite-land-cover?tab=overview
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:32662
  description: 'Flag to mark areas that could not be classified. Two values are used:
    0, 1; respectively meaning: not_processed, processed.'
  download_url: null
  format: null
  id: resource_ElzHcgz1
  media_type: application/netcdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 300
  temporal:
    central_year: null
    duration: null
    end: '2022-01-01'
    start: '1992-01-01'
  temporal_resolution: P1Y
  title: Processed flag
- access_url: https://cds.climate.copernicus.eu/datasets/satellite-land-cover?tab=overview
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:32662
  description: Number of valid satellite observations that have contributed to each
    pixel's classification
  download_url: null
  format: null
  id: resource_3kGbDusD
  media_type: application/netcdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 300
  temporal:
    central_year: null
    duration: null
    end: '2022-01-01'
    start: '1992-01-01'
  temporal_resolution: P1Y
  title: Observation count
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-esacci_landcover
spatial:
  bbox:
  - -180
  - -90
  - 180
  - 90
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal: null
temporal_resolution: null
title: Land cover classification gridded maps from 1992 to present derived from satellite
  observations
version: 2.1.1
vulnerability: null
---
