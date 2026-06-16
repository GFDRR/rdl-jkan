---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-al-zaatari-refugee-camp-mafraq-governorate-jordan-november-19-2014
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-al-zaatari-refugee-camp-mafraq-governorate-jordan-november-19-2014
dataset_id: rdls_exp-jorsyr_unosat_geodataupdatealzaatariref_20141119
description: 'This map illustrates satellite-detected shelters and other buildings
  at the Al Zaatari refugee camp in Mafraq Governorate, Jordan. As of 11 November
  2014 a total of 29,243 shelters were detected as well as 1,915 infrastructure and
  support buildings within the 534.4 hectares of the camp. Between 06 July 2014 and
  11 November 2014, a total of 2,779 shelters closed or were moved, and a total of
  1,910 shelters were constructed, and the number of shelters has thus decreased by
  about 739 since the previous UNITAR/UNOSAT assessment. This indicates an approximate
  2.5% decrease in the number of shelters between 06 July 2014 and 11 November 2014.
  This is a preliminary analysis and has not yet been validated in the field; structure
  locations subject to a spatial error margin of +/- three meters. Shelters grouped
  under plastic sheeting were estimated by average household size and may be a source
  of error. Please send ground feedback to UNITAR/UNOSAT.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/geodata-of-al-zaatari-refugee-camp-mafraq-governorate-jordan-november-19-2014]'
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
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: UNOSAT analysts manually reviewed and compared satellite imagery from
    06 July 2014 and 11 November 2014 to detect shelter and infrastructure buildings
    at Al Zaatari camp, classifying structures by type and status. The resulting geodataset
    contains 29,243 shelters and 1,915 support buildings with confidence ratings and
    validation flags, enabling temporal tracking of camp population infrastructure
    changes.
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
- href: https://data.humdata.org/dataset/geodata-of-al-zaatari-refugee-camp-mafraq-governorate-jordan-november-19-2014
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
  description: 'Geodata of UPDATE: AL Zaatari Refugee camp, Mafraq Governorate, Jordan
    (Shapefile)'
  download_url: https://cern.ch/unosat-maps/SY/CE20130604SYR/Al_Zaatari_Shelters_20141111_shp.zip
  format: null
  id: resource_b846b3d4
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Al_Zaatari_Shelters_20141111_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Geodata of UPDATE: AL Zaatari Refugee camp, Mafraq Governorate, Jordan
    (Shapefile)'
  download_url: https://cern.ch/unosat-maps/SY/CE20130604SYR/Al_Zaatari_20141111.gdb.zip
  format: null
  id: resource_a8e88f4d
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Al_Zaatari_20141111.gdb.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-jorsyr_unosat_geodataupdatealzaatariref_20141119
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
  start: '2014-11-19'
temporal_resolution: null
title: 'Geodata of UPDATE: AL Zaatari Refugee camp, Mafraq Governorate, Jordan'
version: null
vulnerability: null
---
