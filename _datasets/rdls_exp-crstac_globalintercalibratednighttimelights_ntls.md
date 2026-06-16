---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Yale University
  url: https://urbanization.yale.edu/data
creator:
  affiliation: null
  email: null
  name: Yale University
  url: https://urbanization.yale.edu/data
dataset_id: rdls_exp-crstac_globalintercalibratednighttimelights_ntls
description: 'Global inter-calibrated nighttime lights (NTLs) have been generated
  from stable NTL annual composite product (version 4) using a novel ''Ridgeline Sampling
  and Regression'' method (Zhang et al., 2016). Before use, all images will need to
  be re-scaled by multiplying pixel values with a scaling factor of 0.01. For more
  information, refer to Zhang et al. (2016) [Source: This metadata record was automatically
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
license: https://spdx.org/licenses/CC-BY-4.0.html
lineage:
  description: Global inter-calibrated nighttime lights (NTLs) have been generated
    from stable NTL annual composite product (version 4) using a novel 'Ridgeline
    Sampling and Regression' method (Zhang et al., 2016). Before use, all images will
    need to be re-scaled by multiplying pixel values with a scaling factor of 0.01.
    For more information, refer to Zhang et al. (2016).
  sources:
  - id: source_underlying_1
    license: null
    name: DMSP data
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
  name: Yale University
  url: https://urbanization.yale.edu/data
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: 10.1109/TGRS.2016.2572724
  id: ref_doi
  name: null
  url: https://doi.org/10.1109/TGRS.2016.2572724
resources:
- access_url: https://climate-risk-data.github.io/climate-risk-stac/stac/exposure-vulnerability/land-use/global-inter-calibrated-nighttime-lights/ntls/ntls.json
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
  title: 'STAC Item: Global inter-calibrated nighttime lights - NTLs'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Global inter-calibrated nighttime lights - NTLs - data file
  download_url: https://www.dropbox.com/s/b1wjqx0iniq0trz/Intercalibrated%20NTL_RSR.7z?dl=0
  format: null
  id: resource_data-file_1
  media_type: image/tiff; application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Global inter-calibrated nighttime lights - NTLs - data file
- access_url: https://doi.org/10.1109/TGRS.2016.2572724
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Global inter-calibrated nighttime lights - NTLs (Web reference)
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
slug: rdls_exp-crstac_globalintercalibratednighttimelights_ntls
spatial:
  bbox:
  - -180.0
  - -65.0
  - 180.0
  - 75.0
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: 926
temporal:
  central_year: null
  duration: null
  end: '2012'
  start: '1992'
temporal_resolution: P1Y
title: Global inter-calibrated nighttime lights - NTLs
version: null
vulnerability: null
---
