---
attributions:
- entity:
    affiliation: null
    email: null
    name: Bing Maps imagery (approx. 2016-2019)
    url: https://data.humdata.org/dataset/ai-building-footprint-in-izabal-guatemala
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: automated-building-detection (rodekruis/510)
    url: https://data.humdata.org/dataset/ai-building-footprint-in-izabal-guatemala
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Netherlands Red Cross - 510
  url: https://data.humdata.org/dataset/ai-building-footprint-in-izabal-guatemala
creator:
  affiliation: null
  email: null
  name: Netherlands Red Cross - 510
  url: https://data.humdata.org/dataset/ai-building-footprint-in-izabal-guatemala
dataset_id: rdls_exp-gtm_nlrc510_aibuildingfootprintizabal_20201127
description: 'Izabal department (GT-IZ), Guatemala: AI predictions of building footprint
  on Bing Maps images (approximately 2016-2019), see https://github.com/rodekruis/automated-building-detection.
  Produced in support to DRRT Guatemala for hurricane Eta and Iota. Coordinate reference
  system: WGS 84 / EPSG:4326. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/ai-building-footprint-in-izabal-guatemala]'
details: Buildings might be missing, complement if possible.
exposure:
- asset_type:
    description: AI-predicted building footprints for Izabal department, Guatemala,
      derived from Bing Maps imagery (approx. 2016-2019) using automated deep learning
      detection
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
      unit: null
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Building footprints were generated using an AI/deep learning model
    (automated-building-detection) applied to Bing Maps imagery from approximately
    2016-2019 over Izabal department, Guatemala. The model produces vector polygon
    predictions of individual building footprints, exported as GeoJSON in WGS84. The
    dataset was produced in support of DRRT Guatemala disaster response operations
    following hurricanes Eta and Iota.
  sources:
  - id: source_1
    license: null
    name: Bing Maps imagery (approx. 2016-2019)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: automated-building-detection (rodekruis/510)
    risk_data_type:
    - exposure
    type: model
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/ai-building-footprint-in-izabal-guatemala
  rel: source
loss:
  losses: []
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://github.com/rodekruis/automated-building-detection
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Izabal department (GT-IZ), Guatemala: AI predictions of building footprint
    on Bing Maps images (approximately 2016-2019), see https://github.com/rodekruis/automated-building-detection.
    Produced in support to DRRT Guatemala for hurricane Eta and Iota. Coordinate reference
    system: WGS 84 / EPSG:4326'
  download_url: https://data.humdata.org/dataset/00a27905-efd2-4ce5-b5d2-6c862ad7d852/resource/4e4b3d3f-6a31-4623-902a-76eea7fc928f/download/buildings-izabal.geojson
  format: null
  id: resource_4e4b3d3f
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: buildings-izabal.geojson
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-gtm_nlrc510_aibuildingfootprintizabal_20201127
spatial:
  bbox: null
  centroid: null
  countries:
  - GTM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2020-11-27'
temporal_resolution: null
title: AI building footprint in Izabal, Guatemala
version: null
vulnerability: null
---
