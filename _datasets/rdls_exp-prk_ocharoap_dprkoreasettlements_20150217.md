---
attributions:
- entity:
    affiliation: null
    email: null
    name: Open Street Map
    url: https://data.humdata.org/dataset/dpr-korea-settlements
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Regional Office for Asia and the Pacific (ROAP)
  url: https://data.humdata.org/dataset/dpr-korea-settlements
creator:
  affiliation: null
  email: null
  name: OCHA Regional Office for Asia and the Pacific (ROAP)
  url: https://data.humdata.org/dataset/dpr-korea-settlements
dataset_id: rdls_exp-prk_ocharoap_dprkoreasettlements_20150217
description: 'This spatial dataset of settlements is a national dataset of 643 villages,
  towns and cities and suburbs across DPR Korea. The attribute information includes
  the location name (in local Korean script concatenated with the English translation),
  OSM id, and the associated province and county administrative name and code. This
  dataset is also referred to as the village or population point dataset and can be
  complemented by the WFP dataset.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/dpr-korea-settlements]'
details: '**Most Recent Changes:** The OSM dataset was intersected with the admin
  2 dataset to assign admin 1 and 2 attribute values to the dataset. **Languages:**
  EN KO'
exposure:
- asset_type:
    description: Spatial inventory of 643 settlements (villages, towns, cities, suburbs)
      across DPR Korea with location names and administrative associations
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
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Settlement point data extracted from Open Street Map for DPR Korea,
    including 643 populated places with attributes for location names (Korean and
    English), OSM identifiers, and administrative hierarchies (province and county
    codes). This spatial inventory serves as a foundational exposure dataset for disaster
    risk assessment.
  sources:
  - id: source_1
    license: null
    name: Open Street Map
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/dpr-korea-settlements
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
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DPR Korea - Settlements (Shapefile)
  download_url: https://data.humdata.org/dataset/c9585460-6776-4210-a5f4-6e1089ddcf03/resource/206bf9f1-1521-4377-9cb4-14b0b53a94e8/download/prk_pplp_osm.zip
  format: null
  id: resource_206bf9f1
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: prk_pplp_osm.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-prk_ocharoap_dprkoreasettlements_20150217
spatial:
  bbox: null
  centroid: null
  countries:
  - PRK
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-02-17'
temporal_resolution: null
title: DPR Korea - Settlements
version: null
vulnerability: null
---
