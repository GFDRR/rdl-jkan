---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: World Resources Institute (WRI)
  url: https://datasets.wri.org/dataset/globalpowerplantdatabase
creator:
  affiliation: null
  email: null
  name: World Resources Institute (WRI)
  url: https://datasets.wri.org/dataset/globalpowerplantdatabase
dataset_id: rdls_exp-crstac_globalpowerplantdatabase_version130june2021
description: 'The database covers approximately 35,000 power plants from 167 countries
  and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal)
  and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries
  contain information on plant capacity, generation, ownership, and fuel type [Source:
  This metadata record was automatically extracted from the STAC catalog climate-risk-stac
  (https://climate-risk-data.github.io/climate-risk-stac/)]'
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
license: https://spdx.org/licenses/CC-BY-4.0.html
lineage:
  description: The Global Power Plant Database is a comprehensive, open source database
    of power plants around the world. It centralizes power plant data to make it easier
    to navigate, compare and draw insights for one's own analysis. The database covers
    approximately 35,000 power plants from 167 countries and includes thermal plants
    (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g.
    hydro, wind, solar). Each power plant is geolocated and entries contain information
    on plant capacity, generation, ownership, and fuel type. It will be continuously
    updated as data becomes available.
  sources:
  - id: source_code_codelink
    license: null
    name: Code link
    risk_data_type: null
    type: model
    url: https://github.com/wri/global-power-plant-database
    used_in: null
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: World Resources Institute (WRI)
  url: https://datasets.wri.org/dataset/globalpowerplantdatabase
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: ref_pub_publicationlink
  name: Publication link
  url: https://files.wri.org/d8/s3fs-public/2021-07/global-power-plant-database-technical-note-v1.3.pdf?VersionId=KNA6zn0E2HgUcEsXhtZuvfAlIqWOjLib
resources:
- access_url: https://climate-risk-data.github.io/climate-risk-stac/stac/exposure-vulnerability/infrastructure/global-power-plant-database/version-130-june-2021/version-130-june-2021.json
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
  spatial_aggregation: feature level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'STAC Item: Global Power Plant Database - version 1.3.0 (June 2021)'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Global Power Plant Database - version 1.3.0 (June 2021) - data file
  download_url: https://wri-dataportal-prod.s3.amazonaws.com/manual/global_power_plant_database_v_1_3.zip
  format: null
  id: resource_data-file_1
  media_type: application/zip
  spatial: null
  spatial_aggregation: feature level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Global Power Plant Database - version 1.3.0 (June 2021) - data file
- access_url: https://files.wri.org/d8/s3fs-public/2021-07/global-power-plant-database-technical-note-v1.3.pdf?VersionId=KNA6zn0E2HgUcEsXhtZuvfAlIqWOjLib
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Global Power Plant Database - version 1.3.0 (June 2021) (Publication
    link)
  download_url: null
  format: Web reference
  id: resource_link_publicationlink
  media_type: null
  spatial: null
  spatial_aggregation: feature level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Publication link
- access_url: https://github.com/wri/global-power-plant-database
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Global Power Plant Database - version 1.3.0 (June 2021) (Code link)
  download_url: null
  format: Web reference
  id: resource_link_codelink
  media_type: null
  spatial: null
  spatial_aggregation: feature level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Code link
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-crstac_globalpowerplantdatabase_version130june2021
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
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026'
  start: '2021'
temporal_resolution: null
title: Global Power Plant Database - version 1.3.0 (June 2021)
version: null
vulnerability: null
---
