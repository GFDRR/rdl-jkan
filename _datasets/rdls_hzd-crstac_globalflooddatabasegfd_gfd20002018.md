---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Cloud to Street
  url: https://global-flood-database.cloudtostreet.ai/#
creator:
  affiliation: null
  email: null
  name: Cloud to Street
  url: https://global-flood-database.cloudtostreet.ai/#
dataset_id: rdls_hzd-crstac_globalflooddatabasegfd_gfd20002018
description: 'The Global Flood Database provides satellite-derived flood footprints
  and depths for 913 floods that occurred between 2000 and 2018. Also covers processes:
  coastal_flood, pluvial_flood (STAC subcategory: "coastal flood,fluvial flood,pluvial
  flood") [Source: This metadata record was automatically extracted from the STAC
  catalog climate-risk-stac (https://climate-risk-data.github.io/climate-risk-stac/)]'
details: null
exposure: []
hazard:
  event_sets_by_hazard_type:
    flood:
    - analysis_type: empirical
      calculation_method: simulated
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://spdx.org/licenses/CC-BY-4.0.html
lineage:
  description: The Global Flood Database provides satellite-derived flood footprints
    and depths for 913 floods that occurred between 2000 and 2018.
  sources:
  - id: source_underlying_1
    license: null
    name: MODIS satellite imagery
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_code_codelink
    license: null
    name: Code link
    risk_data_type: null
    type: model
    url: https://github.com/cloudtostreet/MODIS_GlobalFloodDatabase
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
  name: Cloud to Street
  url: https://global-flood-database.cloudtostreet.ai/#
purpose: Download per event possible. The data do not differentiate flood types.
referenced_by:
- author_names: null
  date_published: null
  doi: 10.1038/s41586-021-03695-w
  id: ref_doi
  name: null
  url: https://doi.org/10.1038/s41586-021-03695-w
resources:
- access_url: https://climate-risk-data.github.io/climate-risk-stac/stac/hazard/flood/global-flood-database-gfd/gfd-2000-2018/gfd-2000-2018.json
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
  title: 'STAC Item: Global Flood Database (GFD) - GFD 2000-2018'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Global Flood Database (GFD) - GFD 2000-2018 - data file
  download_url: https://global-flood-database.cloudtostreet.ai/#
  format: null
  id: resource_data-file_1
  media_type: image/tiff; application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Global Flood Database (GFD) - GFD 2000-2018 - data file
- access_url: https://doi.org/10.1038/s41586-021-03695-w
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Global Flood Database (GFD) - GFD 2000-2018 (Web reference)
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
- access_url: https://github.com/cloudtostreet/MODIS_GlobalFloodDatabase
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Global Flood Database (GFD) - GFD 2000-2018 (Code link)
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
- hazard
schema: rdls-10
slug: rdls_hzd-crstac_globalflooddatabasegfd_gfd20002018
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
spatial_resolution: 249
temporal:
  central_year: null
  duration: null
  end: '2018'
  start: '2000'
temporal_resolution: null
title: Global Flood Database (GFD) - GFD 2000-2018
version: null
vulnerability: null
---
