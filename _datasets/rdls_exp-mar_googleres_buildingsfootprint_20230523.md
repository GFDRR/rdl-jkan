---
attributions:
- entity:
    affiliation: null
    email: null
    name: Google Research Open Buildings
    url: https://data.humdata.org/dataset/openbuildings_morocco_earthquake_footprint
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Google Research
  url: https://data.humdata.org/dataset/openbuildings_morocco_earthquake_footprint
creator:
  affiliation: null
  email: null
  name: Google Research
  url: https://data.humdata.org/dataset/openbuildings_morocco_earthquake_footprint
dataset_id: rdls_exp-mar_googleres_buildingsfootprint_20230523
description: 'A dataset of building footprints in Morocco, in the area of the 8 September
  earthquake. Footprint as of May 2023. Building footprints are useful for a range
  of important applications, from population estimation, urban planning and humanitarian
  response, to environmental and climate science. This large-scale open dataset contains
  the outlines of buildings derived from high-resolution satellite imagery in order
  to support these types of uses. For more info visit open buildings FAQ https://sites.research.google/open-buildings/#faq.
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/openbuildings_morocco_earthquake_footprint]'
details: The data is shared under the Creative Commons Attribution (CC BY-4.0) license
  and the Open Data Commons Open Database License (ODbL) v1.0 license. As the user,
  you can pick which of the two licenses you prefer and use the data under the terms
  of that license. However, please note the liability disclaimer in the footnotes
  1 . https://sites.research.google/open-buildings/#faq
exposure:
- asset_type:
    description: Building footprints derived from high-resolution satellite imagery
      in Morocco earthquake epicenter area
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
      quantity_kind: count
      unit: count
hazard: null
license: CC-BY-4.0
lineage:
  description: Building footprints were extracted from high-resolution satellite imagery
    as of May 2023 covering the 8 September earthquake epicenter region in Morocco.
    The dataset provides vector outlines of building structures to support population
    estimation, urban planning, and humanitarian response applications.
  sources:
  - id: source_1
    license: null
    name: Google Research Open Buildings
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/openbuildings_morocco_earthquake_footprint
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Registry
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: A dataset of building footprints in Morocco, in the area of the 8 September
    earthquake. Footprint as of May 2023. For more info visit open buildings FAQ https://sites.research.google/open-buildings/#faq
    The file contains centroids, building footprints (as WKT), and Plus codes.
  download_url: https://data.humdata.org/dataset/c6059279-4521-4b39-8b18-d43aedc012c3/resource/6af2ee44-1807-4fb7-a647-a42fc7ffbff0/download/open_buildings_v3_morocco_epicenter.csv.gz
  format: null
  id: resource_6af2ee44
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: open_buildings_v3_Morocco_Earthquake_Epicenter.csv.gz
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: A smaller version of the dataset which contains only points representing
    the buildings. For more info visit open buildings FAQ https://sites.research.google/open-buildings/#faq
  download_url: https://data.humdata.org/dataset/c6059279-4521-4b39-8b18-d43aedc012c3/resource/7f877f69-2826-4265-b4b7-48f27e1fc3e9/download/points_only.zip
  format: null
  id: resource_7f877f69
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: points_only.csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: A version of the dataset with building footprints in geopackage format.
    For more info visit open buildings FAQ https://sites.research.google/open-buildings/#faq
  download_url: https://data.humdata.org/dataset/c6059279-4521-4b39-8b18-d43aedc012c3/resource/4fdbb7d1-9248-4244-934f-a790dae49906/download/building_footprints.zip
  format: null
  id: resource_4fdbb7d1
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: building_footprints.gpkg.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-mar_googleres_buildingsfootprint_20230523
spatial:
  bbox: null
  centroid: null
  countries:
  - MAR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-05-23'
temporal_resolution: null
title: 'Morocco: Buildings Footprint'
version: null
vulnerability: null
---
