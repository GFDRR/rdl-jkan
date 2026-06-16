---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Zenodo
  url: https://zenodo.org/records/4957647
creator:
  affiliation: null
  email: null
  name: Zenodo
  url: https://zenodo.org/records/4957647
dataset_id: rdls_exp-crstac_criticalinfrastructurespatialindexcisi_types025decdeg
description: 'CISI infrastructure types at a spatial resolution of 0.25 decimal degrees
  [Source: This metadata record was automatically extracted from the STAC catalog
  climate-risk-stac (https://climate-risk-data.github.io/climate-risk-stac/)]'
details: null
exposure:
- asset_type:
    description: infrastructure footprints
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: CC-BY-4.0
lineage:
  description: The Critical Infrastructure Spatial Index (CISI) is calculated from
    39 critical infrastructure types (e.g. airports, clinics, landfills, reservoirs,
    schools) downloaded from Open Street Map (OSM).
  sources:
  - id: source_underlying_1
    license: null
    name: Open Street Map (OSM)
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
    url: https://doi.org/10.5281/zenodo.4819989
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
  url: https://zenodo.org/records/4957647
purpose: The CISI is developed from OSM data and its spatial coverage depends on the
  completeness of OSM records.
referenced_by:
- author_names: null
  date_published: null
  doi: 10.1038/s41597-022-01218-4
  id: ref_doi
  name: null
  url: https://doi.org/10.1038/s41597-022-01218-4
resources:
- access_url: https://climate-risk-data.github.io/climate-risk-stac/stac/exposure-vulnerability/infrastructure/critical-infrastructure-spatial-index-cisi/types-025-dec-deg/types-025-dec-deg.json
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
  title: 'STAC Item: Critical Infrastructure Spatial Index (CISI) - Types 0.25 dec
    deg'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Critical Infrastructure Spatial Index (CISI) - Types 0.25 dec deg -
    data file
  download_url: https://zenodo.org/records/4957647/files/Amount_of_infrastructure.zip?download=1
  format: null
  id: resource_data-file_1
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Critical Infrastructure Spatial Index (CISI) - Types 0.25 dec deg - data
    file
- access_url: https://doi.org/10.1038/s41597-022-01218-4%C2%A0
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Critical Infrastructure Spatial Index (CISI) - Types 0.25 dec deg (Web
    reference)
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
- access_url: https://doi.org/10.5281/zenodo.4819989
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Critical Infrastructure Spatial Index (CISI) - Types 0.25 dec deg (Code
    link)
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
slug: rdls_exp-crstac_criticalinfrastructurespatialindexcisi_types025decdeg
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
spatial_resolution: 27750
temporal:
  central_year: null
  duration: null
  end: '2021'
  start: '2021'
temporal_resolution: null
title: Critical Infrastructure Spatial Index (CISI) - Types 0.25 dec deg
version: null
vulnerability: null
---
