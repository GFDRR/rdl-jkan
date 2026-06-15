---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-al-zaatari-refugee-camp-mafraq-governorate-jordan-july-21-2014
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-al-zaatari-refugee-camp-mafraq-governorate-jordan-july-21-2014
dataset_id: rdls_exp-jorsyr_unosat_geodataupdatealzaatariref_20140721
description: 'This map illustrates satellite-detected shelters and other buildings
  at the Al Zaatari refugee camp in Mafraq Governorate, Jordan. As of 06 July 2014
  a total of 29,982 shelters were detected as well as 1,880 infrastructure and support
  buildings within the 534.4 hectares of the camp. Between 06 April 2014 and 06 July
  2014, a total of 4,257 shelters closed or were moved, and a total of 2,774 shelters
  were constructed, and the number of shelters has thus decreased by about 1,298 since
  the previous UNITAR/UNOSAT assessment. This indicates an approximate 4.1% decrease
  in the number of shelters between 06 April 2014 and 06 July 2014. This is a preliminary
  analysis and has not yet been validated in the field; structure locations subject
  to a spatial error margin of +/- three meters. Shelters grouped under plastic sheeting
  were estimated by average household size and may be a source of error. Please send
  ground feedback to UNITAR/UNOSAT.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-al-zaatari-refugee-camp-mafraq-governorate-jordan-july-21-2014]'
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
    description: Satellite-detected shelter and infrastructure buildings at Al Zaatari
      refugee camp with temporal change tracking
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
- asset_type:
    description: Refugee population inferred from shelter count at Al Zaatari camp
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_2
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: UNOSAT analysts manually interpreted satellite imagery acquired on
    06 July 2014, detecting and mapping individual shelter and infrastructure building
    footprints at Al Zaatari refugee camp. Multi-temporal comparison with previous
    imagery from 06 April 2014 enabled tracking of shelter construction, closure,
    and relocation events to quantify camp population dynamics.
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
- href: https://data.humdata.org/dataset/geodata-of-al-zaatari-refugee-camp-mafraq-governorate-jordan-july-21-2014
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
  description: 'Geodata of UPDATE: AL ZAATARI REFUGEE CAMP, MAFRAQ GOVERNORATE, JORDAN
    (Shapefile)'
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SY/CE20130604SYR/Al_Zaatari_20140706.shp.zip
  format: null
  id: resource_a674e887
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Al_Zaatari_20140706.shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Geodata of UPDATE: AL ZAATARI REFUGEE CAMP, MAFRAQ GOVERNORATE, JORDAN
    (Shapefile)'
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SY/CE20130604SYR/Al_Zaatari_20140706.gdb.zip
  format: null
  id: resource_a4fd6ab2
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Al_Zaatari_20140706.gdb.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-jorsyr_unosat_geodataupdatealzaatariref_20140721
spatial:
  bbox: null
  centroid: null
  countries:
  - SYR
  - JOR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2014-07-21'
temporal_resolution: null
title: 'Geodata of UPDATE: AL ZAATARI REFUGEE CAMP, MAFRAQ GOVERNORATE, JORDAN'
version: null
vulnerability: null
---
