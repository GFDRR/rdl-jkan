---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-idp-shelter-density-in-daynile-and-dharkenley-district-mogadishu-november-10-2014
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-idp-shelter-density-in-daynile-and-dharkenley-district-mogadishu-november-10-2014
dataset_id: rdls_exp-som_unosat_geodataupdateidpshelterde_20141110
description: 'This map illustrates IDPs structure density in the Daynile and Dharkenley
  districts in Mogadishu, Somalia, as detected in a Pleiades satellite image collected
  on 9 October 2014. UNOSAT analysis detected a total of 34,806 IDPs structures in
  these areas, which includes 14,655 temporary housing structures, 213 tukul-style
  structures, 4,428 shelters and 15,510 buuls. It is likely that subtle differences
  between temporary housing structures and shelters will lead to significant confusion
  between those two classes, though the overall structural count is accurate. This
  is a preliminary analysis and has not yet been validated in the field. Please send
  ground feedback to UNITAR / UNOSAT. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-idp-shelter-density-in-daynile-and-dharkenley-district-mogadishu-november-10-2014]'
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
    description: IDP shelter structures classified by type (temporary housing, tukul,
      shelters, buuls) detected via satellite imagery
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
  description: UNOSAT analysts reviewed Pleiades satellite imagery from October 2014
    and compared temporal images to detect and classify IDP shelter structures in
    Daynile and Dharkenley districts. Structures were categorized into four types
    (temporary housing, tukul, shelters, buuls) through visual interpretation, resulting
    in a spatial inventory of 34,806 structures with confidence levels and validation
    flags.
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
- href: https://data.humdata.org/dataset/geodata-of-idp-shelter-density-in-daynile-and-dharkenley-district-mogadishu-november-10-2014
  rel: source
loss: null
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
  description: 'Geodata of UPDATE: IDP Shelter density in Daynile and Dharkenley District,
    Mogadishu, Somalia (Shapefile)'
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SO/CE20130710SOM/CE20130710SOM_DD_shp.zip
  format: null
  id: resource_e5ae7eb1
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20130710SOM_DD_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Geodata of UPDATE: IDP Shelter density in Daynile and Dharkenley District,
    Mogadishu, Somalia (Shapefile)'
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SO/CE20130710SOM/CE20130710SOM_DD.gdb.zip
  format: null
  id: resource_0f29d5fc
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20130710SOM_DD.gdb.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-som_unosat_geodataupdateidpshelterde_20141110
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
  start: '2014-11-10'
temporal_resolution: null
title: 'Geodata of UPDATE: IDP Shelter density in Daynile and Dharkenley District,
  Mogadishu, Somalia'
version: null
vulnerability: null
---
