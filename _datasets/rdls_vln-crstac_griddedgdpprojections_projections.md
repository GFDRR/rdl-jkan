---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Figshare
  url: https://gcp-tsukuba.github.io/SSP-downscale/#downscaling-gdp
creator:
  affiliation: null
  email: null
  name: Figshare
  url: https://gcp-tsukuba.github.io/SSP-downscale/#downscaling-gdp
dataset_id: rdls_vln-crstac_griddedgdpprojections_projections
description: 'Estimated GDPs by 1/12-degree grids during 1850-2100 by 10 year intervals.
  In the estimation, national GDP data (past data until 2010; future projection under
  SSPs after 2020) is downscaled considering spatial and economic interactions among
  cities, urban growth patterns compatible with SSPs, and other auxiliary geographic
  data (land cover, road network, etc.). Climate scenarios (as published): "SSPs"
  [Source: This metadata record was automatically extracted from the STAC catalog
  climate-risk-stac (https://climate-risk-data.github.io/climate-risk-stac/)]'
details: null
exposure: []
hazard: null
license: https://spdx.org/licenses/CC-BY-4.0.html
lineage:
  description: Estimated GDPs by 1/12-degree grids during 1850-2100 by 10 year intervals.
    In the estimation, national GDP data (past data until 2010; future projection
    under SSPs after 2020) is downscaled considering spatial and economic interactions
    among cities, urban growth patterns compatible with SSPs, and other auxiliary
    geographic data (land cover, road network, etc.).
  sources:
  - id: source_underlying_1
    license: null
    name: Several data sources (see publication for further details)
    risk_data_type:
    - vulnerability
    type: dataset
    url: null
    used_in: vulnerability
  - id: source_code_codelink
    license: null
    name: Code link
    risk_data_type: null
    type: model
    url: https://gcp-tsukuba.github.io/SSP-downscale/#code-for-visualization
    used_in: null
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Figshare
  url: https://gcp-tsukuba.github.io/SSP-downscale/#downscaling-gdp
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: 10.3389/fbuil.2021.760306
  id: ref_doi
  name: null
  url: https://doi.org/10.3389/fbuil.2021.760306
resources:
- access_url: https://climate-risk-data.github.io/climate-risk-stac/stac/exposure-vulnerability/population/gridded-gdp-projections/projections/projections.json
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
  download_url: https://figshare.com/ndownloader/files/22078776
  format: null
  id: resource_data-file_1
  media_type: image/tiff; application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Projections - data file
- access_url: https://doi.org/10.3389/fbuil.2021.760306
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
- access_url: https://gcp-tsukuba.github.io/SSP-downscale/#code-for-visualization
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
- vulnerability
schema: rdls-10
slug: rdls_vln-crstac_griddedgdpprojections_projections
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
spatial_resolution: 9250
temporal:
  central_year: null
  duration: null
  end: '2100'
  start: '1850'
temporal_resolution: P10Y
title: Projections
version: null
vulnerability: null
---
