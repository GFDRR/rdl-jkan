---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: WorldPop
  url: https://hub.worldpop.org/
creator:
  affiliation: null
  email: null
  name: WorldPop
  url: https://hub.worldpop.org/
dataset_id: rdls_exp-crstac_worldpop_populationunconstrained30arcse
description: 'Estimated total number of people per grid-cell. The dataset is available
  to download in Geotiff format. The projection is Geographic Coordinate System, WGS84.
  The units are number of people per pixel. The mapping approach is Random Forest-based
  dasymetric redistribution [Source: This metadata record was automatically extracted
  from the STAC catalog climate-risk-stac (https://climate-risk-data.github.io/climate-risk-stac/)]'
details: null
exposure:
- asset_type:
    description: population number
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: https://spdx.org/licenses/CC-BY-4.0.html
lineage:
  description: Open access spatial demographic datasets built using transparent approaches.
  sources:
  - id: source_code_codelink
    license: null
    name: Code link
    risk_data_type: null
    type: model
    url: https://github.com/wpgp/popRF
    used_in: null
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: WorldPop
  url: https://hub.worldpop.org/
purpose: download per year
referenced_by:
- author_names: null
  date_published: null
  doi: 10.1080/20964471.2019.1625151
  id: ref_doi
  name: null
  url: https://doi.org/10.1080/20964471.2019.1625151
resources:
- access_url: https://climate-risk-data.github.io/climate-risk-stac/stac/exposure-vulnerability/population/worldpop/population-unconstrained-30-arc-seconds/population-unconstrained-30-arc-seconds.json
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
  title: 'STAC Item: WorldPop - Population (unconstrained) 30 arc seconds'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: WorldPop - Population (unconstrained) 30 arc seconds - data file
  download_url: https://hub.worldpop.org/geodata/listing?id=64
  format: null
  id: resource_data-file_1
  media_type: image/tiff; application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: WorldPop - Population (unconstrained) 30 arc seconds - data file
- access_url: https://doi.org/10.1080/20964471.2019.1625151
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: WorldPop - Population (unconstrained) 30 arc seconds (Web reference)
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
- access_url: https://github.com/wpgp/popRF
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: WorldPop - Population (unconstrained) 30 arc seconds (Code link)
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
slug: rdls_exp-crstac_worldpop_populationunconstrained30arcse
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
  end: '2020'
  start: '2000'
temporal_resolution: P1Y
title: WorldPop - Population (unconstrained) 30 arc seconds
version: null
vulnerability: null
---
