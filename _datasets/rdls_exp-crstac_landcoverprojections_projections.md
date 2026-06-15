---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Figshare
  url: https://figshare.com/articles/dataset/Global_LULC_projection_dataset_from_2020_to_2100_at_a_1km_resolution/23542860
creator:
  affiliation: null
  email: null
  name: Figshare
  url: https://figshare.com/articles/dataset/Global_LULC_projection_dataset_from_2020_to_2100_at_a_1km_resolution/23542860
dataset_id: rdls_exp-crstac_landcoverprojections_projections
description: 'Land cover projections under SSP-RCP combinations 2020-2100 with a spatial
  resolution of ~1 km. Climate scenarios (as published): "SSP-RCP combinations" [Source:
  This metadata record was automatically extracted from the STAC catalog climate-risk-stac
  (https://climate-risk-data.github.io/climate-risk-stac/)]'
details: null
exposure:
- asset_type:
    description: land use/land cover footprints
    id: natural_environment
    scheme: null
    title: null
    uri: null
  category: natural_environment
  id: exposure_1
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: square_metre
hazard: null
license: https://spdx.org/licenses/CC-BY-4.0.html
lineage:
  description: Land cover projections under SSP-RCP combinations 2020-2100 with a
    spatial resolution of ~1 km
  sources:
  - id: source_code_codelink
    license: null
    name: Code link
    risk_data_type: null
    type: model
    url: https://github.com/HPSCIL/Patch-generating_Land_Use_Simulation_Model
    used_in: null
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss:
  losses: []
project: null
publisher:
  affiliation: null
  email: null
  name: Figshare
  url: https://figshare.com/articles/dataset/Global_LULC_projection_dataset_from_2020_to_2100_at_a_1km_resolution/23542860
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: 10.1038/s41597-023-02637-7
  id: ref_doi
  name: null
  url: https://doi.org/10.1038/s41597-023-02637-7
resources:
- access_url: https://climate-risk-data.github.io/climate-risk-stac/stac/exposure-vulnerability/land-use/land-cover-projections/projections/projections.json
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
  title: 'STAC Item: Projections'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Projections - data file
  download_url: https://figshare.com/ndownloader/articles/23542860/versions/1
  format: null
  id: resource_data-file_1
  media_type: image/tiff; application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Projections - data file
- access_url: https://doi.org/10.1038/s41597-023-02637-7
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Projections (Web reference)
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
- access_url: https://github.com/HPSCIL/Patch-generating_Land_Use_Simulation_Model
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Projections (Code link)
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
slug: rdls_exp-crstac_landcoverprojections_projections
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
  end: '2100'
  start: '2020'
temporal_resolution: P10Y
title: Projections
version: null
vulnerability: null
---
