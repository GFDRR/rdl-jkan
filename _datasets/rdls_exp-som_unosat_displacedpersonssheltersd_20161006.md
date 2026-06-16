---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/displaced-persons-shelters-in-dalxiska-somalia
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/displaced-persons-shelters-in-dalxiska-somalia
dataset_id: rdls_exp-som_unosat_displacedpersonssheltersd_20161006
description: 'This map illustrates satellite-detected areas of displaced persons shelters
  in the Dalxiska settlement, north of Kismayo, Lower Juba, Somalia. UNITAR-UNOSAT
  analysis of WorldView-3 satellite imagery acquired 08 September 2016 revealed a
  total of 2,426 shelters as well as 200 infrastructure and support buildings within
  the compound. A new shelter zone, labeled camp 2 on the map, is possibly planned
  north of the main settlement. To the south, camp 1 extends into the town of Dalxiska,
  often blending in to the city structures. This is a preliminary analysis and has
  not yet been validated in the field. Please send ground feedback to UNITAR - UNOSAT..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/displaced-persons-shelters-in-dalxiska-somalia]'
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure:
- asset_type:
    description: Displaced persons shelters and support infrastructure detected via
      satellite imagery in Dalxiska settlement
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
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts interpreted WorldView-3 satellite imagery acquired
    on 8 September 2016 of the Dalxiska displaced persons settlement in Lower Juba,
    Somalia, manually identifying and mapping shelter structures and support infrastructure
    through visual analysis and comparison with reference imagery. The resulting geodatabase
    contains spatial footprints and attributes of detected shelters classified by
    camp zone, status, and confidence level.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/displaced-persons-shelters-in-dalxiska-somalia
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
  description: Somalia - Displaced Persons' Shelters in Dalxiska (Zipped geodatabase)
  download_url: https://cern.ch/unosat-maps/SO/CE20130710SOM/CE20130710SOM_Dalxiska_20160908.gdb.zip
  format: Geodatabase
  id: resource_8d2b2e88
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20130710SOM_Dalxiska_20160908.gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Somalia - Displaced Persons' Shelters in Dalxiska (Shapefile)
  download_url: https://cern.ch/unosat-maps/SO/CE20130710SOM/CE20130710SOM_Dalxiska_20160908_shp.zip
  format: null
  id: resource_4fe34740
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20130710SOM_Dalxiska_20160908_shp.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-som_unosat_displacedpersonssheltersd_20161006
spatial:
  bbox: null
  centroid: null
  countries:
  - SOM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2016-10-06'
temporal_resolution: null
title: Somalia - Displaced Persons' Shelters in Dalxiska
version: null
vulnerability: null
---
