---
attributions: []
catalog: Zenodo
contact_point:
  affiliation: null
  email: null
  name: Globus
  url: https://data.pnnl.gov/group/nodes/dataset/33335
creator:
  affiliation: null
  email: null
  name: Globus
  url: https://data.pnnl.gov/group/nodes/dataset/33335
dataset_id: rdls_exp-crstac_gcamdemeterlanduse_projections
description: 'The dataset includes the projected global gridded land cover (excluding
  the Antarctic) for the period of 2015-2100 at 0.05-degree resolution and 5-year
  time step under fifteen SSP-RCP scenarios driven by five GCMs (i.e., gfdl, hadgem,
  ipsl, miroc, and noresm), using the Global Change Analysis Model (GCAM) and a geospatial
  downscaling model (Demeter). Climate scenarios (as published): "SSP-RCP combinations"
  [Source: This metadata record was automatically extracted from the STAC catalog
  climate-risk-stac (https://climate-risk-data.github.io/climate-risk-stac/)]'
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
license: ODbL-1.0
lineage:
  description: The dataset includes the projected global gridded land cover (excluding
    the Antarctic) for the period of 2015-2100 at 0.05-degree resolution and 5-year
    time step under fifteen SSP-RCP scenarios driven by five GCMs (i.e., gfdl, hadgem,
    ipsl, miroc, and noresm), using the Global Change Analysis Model (GCAM) and a
    geospatial downscaling model (Demeter).
  sources:
  - id: source_underlying_1
    license: null
    name: Several data sources (see publication for further details)
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
    url: https://zenodo.org/records/3954113
    used_in: null
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Globus
  url: https://data.pnnl.gov/group/nodes/dataset/33335
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: 10.1038/s41597-020-00669-x
  id: ref_doi
  name: null
  url: https://doi.org/10.1038/s41597-020-00669-x
resources:
- access_url: https://climate-risk-data.github.io/climate-risk-stac/stac/exposure-vulnerability/land-use/gcam-demeter-land-use/projections/projections.json
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
  title: 'STAC Item: GCAM-Demeter land use - Projections'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: GCAM-Demeter land use - Projections - data file
  download_url: https://g-83fdd0.1beed.03c0.data.globus.org/cartuids/34852_f03e1476adbe5ca1a36b109882405281.tar
  format: null
  id: resource_data-file_1
  media_type: application/x-netcdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GCAM-Demeter land use - Projections - data file
- access_url: https://doi.org/10.1038/s41597-020-00669-x
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: GCAM-Demeter land use - Projections (Web reference)
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
- access_url: https://zenodo.org/records/3954113
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: GCAM-Demeter land use - Projections (Code link)
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
slug: rdls_exp-crstac_gcamdemeterlanduse_projections
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
spatial_resolution: 5550
temporal:
  central_year: null
  duration: null
  end: '2100'
  start: '2015'
temporal_resolution: P5Y
title: GCAM-Demeter land use - Projections
version: null
vulnerability: null
---
