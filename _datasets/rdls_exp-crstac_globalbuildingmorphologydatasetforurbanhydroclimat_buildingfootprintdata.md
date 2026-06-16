---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Zenodo
  url: https://doi.org/10.5281/zenodo.10396451
creator:
  affiliation: null
  email: null
  name: Zenodo
  url: https://doi.org/10.5281/zenodo.10396451
dataset_id: rdls_exp-crstac_globalbuildingmorphologydatasetforurbanhydroclimat_buildingfootprintdata
description: 'The BF_100m contains the building footprint files where each file is
  named as BF_{lon_start}_{lon_end}_{lat_start}_{lat_end}.tif [Source: This metadata
  record was automatically extracted from the STAC catalog climate-risk-stac (https://climate-risk-data.github.io/climate-risk-stac/)]'
details: null
exposure:
- asset_type:
    description: building footprints
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
      quantity_kind: count
      unit: count
hazard: null
license: https://spdx.org/licenses/CC-BY-4.0.html
lineage:
  description: GLobAl building MOrphology dataset for URban climate modelling (GLAMOUR)
    offers the building footprint and height files at the resolution of 100 m in global
    urban centers.
  sources:
  - id: source_underlying_1
    license: null
    name: Sentinel
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_underlying_2
    license: null
    name: GPWv4
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_underlying_3
    license: null
    name: GHSL
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_code_codelink
    license: null
    name: Code link
    risk_data_type: null
    type: model
    url: https://doi.org/10.5281/zenodo.10396450
    used_in: null
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Zenodo
  url: https://doi.org/10.5281/zenodo.10396451
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: 10.1038/s41597-024-03446-2
  id: ref_doi
  name: null
  url: https://doi.org/10.1038/s41597-024-03446-2
resources:
- access_url: https://climate-risk-data.github.io/climate-risk-stac/stac/exposure-vulnerability/buildings/global-building-morphology-dataset-for-urban-hydroclimate-modelling-glamour/building-footprint-data/building-footprint-data.json
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
  title: 'STAC Item: GLobAl building MOrphology dataset for URban hydroclimate modelling
    (GLAMOUR) - Building footprint data'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: GLobAl building MOrphology dataset for URban hydroclimate modelling
    (GLAMOUR) - Building footprint data - data file
  download_url: https://zenodo.org/records/10396451/files/BF_100m.zip?download=1
  format: null
  id: resource_data-file_1
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GLobAl building MOrphology dataset for URban hydroclimate modelling (GLAMOUR)
    - Building footprint data - data file
- access_url: https://doi.org/10.1038/s41597-024-03446-2
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: GLobAl building MOrphology dataset for URban hydroclimate modelling
    (GLAMOUR) - Building footprint data (Web reference)
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
- access_url: https://doi.org/10.5281/zenodo.10396450
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: GLobAl building MOrphology dataset for URban hydroclimate modelling
    (GLAMOUR) - Building footprint data (Code link)
  download_url: null
  format: Web reference
  id: resource_link_codelink
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Code link
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-crstac_globalbuildingmorphologydatasetforurbanhydroclimat_buildingfootprintdata
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
spatial_resolution: 100
temporal:
  central_year: null
  duration: null
  end: '2020'
  start: '2020'
temporal_resolution: null
title: GLobAl building MOrphology dataset for URban hydroclimate modelling (GLAMOUR)
  - Building footprint data
version: null
vulnerability: null
---
