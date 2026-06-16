---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Figshare
  url: https://doi.org/10.6084/m9.figshare.9828827.v2
creator:
  affiliation: null
  email: null
  name: Figshare
  url: https://doi.org/10.6084/m9.figshare.9828827.v2
dataset_id: rdls_exp-crstac_harmonizedglobalnighttimelightdatasetdmspntl_dmspntl
description: 'This is an integrated and consistent nighttime lights (NTL) dataset
  at the global scale that harmonizes the inter-calibrated NTL observations from the
  DMSP data (1992-2013) and the simulated DMSP-like NTL observations from the VIIRS
  data (2014-2021) [Source: This metadata record was automatically extracted from
  the STAC catalog climate-risk-stac (https://climate-risk-data.github.io/climate-risk-stac/)]'
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
license: https://spdx.org/licenses/CC-BY-4.0.html
lineage:
  description: This is an integrated and consistent nighttime lights (NTL) dataset
    at the global scale that harmonizes the inter-calibrated NTL observations from
    the DMSP data (1992-2013) and the simulated DMSP-like NTL observations from the
    VIIRS data (2014-2021)
  sources:
  - id: source_underlying_1
    license: null
    name: DMSP and VIIRS data
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
  name: Figshare
  url: https://doi.org/10.6084/m9.figshare.9828827.v2
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: 10.1038/s41597-020-0510-y
  id: ref_doi
  name: null
  url: https://doi.org/10.1038/s41597-020-0510-y
resources:
- access_url: https://climate-risk-data.github.io/climate-risk-stac/stac/exposure-vulnerability/land-use/harmonized-global-nighttime-light-dataset-dmsp-ntl/dmsp-ntl/dmsp-ntl.json
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
  title: 'STAC Item: DMSP NTL'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: DMSP NTL - data file
  download_url: https://figshare.com/ndownloader/articles/9828827/versions/8
  format: null
  id: resource_data-file_1
  media_type: image/tiff; application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DMSP NTL - data file
- access_url: https://doi.org/10.1038/s41597-020-0510-y
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DMSP NTL (Web reference)
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
slug: rdls_exp-crstac_harmonizedglobalnighttimelightdatasetdmspntl_dmspntl
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
spatial_resolution: 926
temporal:
  central_year: null
  duration: null
  end: '2021'
  start: '1992'
temporal_resolution: P1Y
title: DMSP NTL
version: null
vulnerability: null
---
