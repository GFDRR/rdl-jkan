---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Zenodo
  url: https://doi.org/10.5281/zenodo.5220816
creator:
  affiliation: null
  email: null
  name: Zenodo
  url: https://doi.org/10.5281/zenodo.5220816
dataset_id: rdls_exp-crstac_globalimpervioussurfacedatasetgisd_gisd30m
description: 'A novel and accurate global 30 m impervious surface dynamic dataset
  (GISD30), a predominant indicator of human settlement, for 1985 to 2020 was produced
  using the spectral generalization method and time-series Landsat imagery, on the
  Google Earth Engine cloud-computing platform [Source: This metadata record was automatically
  extracted from the STAC catalog climate-risk-stac (https://climate-risk-data.github.io/climate-risk-stac/)]'
details: null
exposure:
- asset_type:
    description: urban/built-up footprints
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: area
      unit: square_metre
hazard: null
license: CC-BY-4.0
lineage:
  description: A novel and accurate global 30 m impervious surface dynamic dataset
    (GISD30), a predominant indicator of human settlement, for 1985 to 2020 was produced
    using the spectral generalization method and time-series Landsat imagery, on the
    Google Earth Engine cloud-computing platform.
  sources:
  - id: source_underlying_1
    license: null
    name: Landsat
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_underlying_2
    license: null
    name: GAIA
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_underlying_3
    license: null
    name: land cover
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Zenodo
  url: https://doi.org/10.5281/zenodo.5220816
purpose: downloadable by tile
referenced_by:
- author_names: null
  date_published: null
  doi: 10.5194/essd-14-1831-2022
  id: ref_doi
  name: null
  url: https://doi.org/10.5194/essd-14-1831-2022
resources:
- access_url: https://climate-risk-data.github.io/climate-risk-stac/stac/exposure-vulnerability/land-use/global-impervious-surface-dataset-gisd/gisd30-m/gisd30-m.json
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Source STAC Item metadata record for this dataset, hosted as part of
    the climate-risk-stac catalogue. Conforms to STAC v1.0.0.
  download_url: null
  format: null
  id: resource_stac_item
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'STAC Item: Global impervious surface dataset (GISD) - GISD30 m'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Global impervious surface dataset (GISD) - GISD30 m - data file
  download_url: https://doi.org/10.5281/zenodo.5220816
  format: null
  id: resource_data-file_1
  media_type: image/tiff; application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Global impervious surface dataset (GISD) - GISD30 m - data file
- access_url: https://doi.org/10.5194/essd-14-1831-2022
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Global impervious surface dataset (GISD) - GISD30 m (Web reference)
  download_url: null
  format: Web reference
  id: resource_link_reference
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Reference
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-crstac_globalimpervioussurfacedatasetgisd_gisd30m
spatial:
  bbox:
  - -180.0
  - -90.0
  - 180.0
  - 90.0
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: 31
temporal:
  central_year: null
  duration: null
  end: '2020'
  start: '1985'
temporal_resolution: P1Y
title: Global impervious surface dataset (GISD) - GISD30 m
version: null
vulnerability: null
---
