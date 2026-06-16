---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Figshare
  url: https://doi.org/10.6084/m9.figshare.16571064
creator:
  affiliation: null
  email: null
  name: Figshare
  url: https://doi.org/10.6084/m9.figshare.16571064
dataset_id: rdls_exp-crstac_humanfootprint_y20002018
description: 'The annual dynamics of the global Human Footprint, the pressure imposed
  on the eco-environment by changing ecological processes and natural landscapes,
  from 2000 to 2018 based on eight variables that reflect different aspects of human
  pressures [Source: This metadata record was automatically extracted from the STAC
  catalog climate-risk-stac (https://climate-risk-data.github.io/climate-risk-stac/)]'
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
  description: The annual dynamics of the global Human Footprint, the pressure imposed
    on the eco-environment by changing ecological processes and natural landscapes,
    from 2000 to 2018 based on eight variables that reflect different aspects of human
    pressures.
  sources:
  - id: source_underlying_1
    license: null
    name: nighttime lights
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_underlying_2
    license: null
    name: ESA CCI land cover
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_underlying_3
    license: null
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_underlying_4
    license: null
    name: OSM
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
    url: https://github.com/HaoweiGis/humanFootprintMapping/
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
  url: https://doi.org/10.6084/m9.figshare.16571064
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: 10.1038/s41597-022-01284-8
  id: ref_doi
  name: null
  url: https://doi.org/10.1038/s41597-022-01284-8
resources:
- access_url: https://climate-risk-data.github.io/climate-risk-stac/stac/exposure-vulnerability/land-use/human-footprint/y2000-2018/y2000-2018.json
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
  title: 'STAC Item: Human footprint - Y2000-2018'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:54009
  description: Human footprint - Y2000-2018 - data file
  download_url: https://figshare.com/ndownloader/articles/16571064/versions/7
  format: null
  id: resource_data-file_1
  media_type: image/tiff; application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Human footprint - Y2000-2018 - data file
- access_url: https://doi.org/10.1038/s41597-022-01284-8
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Human footprint - Y2000-2018 (Web reference)
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
- access_url: https://github.com/HaoweiGis/humanFootprintMapping/
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Human footprint - Y2000-2018 (Code link)
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
slug: rdls_exp-crstac_humanfootprint_y20002018
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
spatial_resolution: 1000
temporal:
  central_year: null
  duration: null
  end: '2018'
  start: '2000'
temporal_resolution: P1Y
title: Human footprint - Y2000-2018
version: null
vulnerability: null
---
