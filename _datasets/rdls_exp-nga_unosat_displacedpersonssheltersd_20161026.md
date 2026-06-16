---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/displaced-persons-shelters-in-dikwa-nigeria
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/displaced-persons-shelters-in-dikwa-nigeria
dataset_id: rdls_exp-nga_unosat_displacedpersonssheltersd_20161026
description: 'This map illustrates satellite-detected areas of displaced persons shelters
  in the Sangaya settlement, Borno state, Nigeria, and in the surrounding town of
  Dikwa. UNITAR-UNOSAT analysis of satellite imagery acquired 29 September 2016 revealed
  a total of 433 shelters and 54 infrastructure and support buildings within the Sangaya
  compound and a total of 2,259 shelters scattered in the surrounding town. A density
  analysis has been performed to highlight the most dense shelters areas (Sangaya
  settlement included), ranging from 400 to 10,500 shelters per square kilometer.
  This is a preliminary analysis and has not yet been validated in the field. Please
  send ground feedback to UNITAR - UNOSAT.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/displaced-persons-shelters-in-dikwa-nigeria]'
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
    description: Displaced persons shelters detected via satellite imagery in Sangaya
      settlement and Dikwa town, classified by shelter status and structure type
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
  description: UNOSAT analysts reviewed satellite imagery acquired on 29 September
    2016, comparing temporal images to detect shelter structures and infrastructure
    in the Sangaya settlement and surrounding Dikwa town. Density analysis was performed
    to identify shelter concentration areas ranging from 400 to 10,500 shelters per
    square kilometer. Results were validated and compiled into geodatabase and shapefile
    formats with shelter-level attributes including confidence, validation status,
    and structure characteristics.
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
- href: https://data.humdata.org/dataset/displaced-persons-shelters-in-dikwa-nigeria
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
  description: Displaced Persons Shelters in Dikwa, Nigeria (Zipped geodatabase)
  download_url: https://cern.ch/unosat-maps/NG/CE20140617NGA/CE20140617NGA_Dikwa_20160929.gdb.zip
  format: Geodatabase
  id: resource_1c1b0771
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20140617NGA_Dikwa_20160929.gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Displaced Persons Shelters in Dikwa, Nigeria (Shapefile)
  download_url: https://cern.ch/unosat-maps/NG/CE20140617NGA/CE20140617NGA_Dikwa_20160929_shp.zip
  format: null
  id: resource_8d7012b3
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20140617NGA_Dikwa_20160929_shp.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-nga_unosat_displacedpersonssheltersd_20161026
spatial:
  bbox: null
  centroid: null
  countries:
  - NGA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2016-10-26'
temporal_resolution: null
title: Displaced Persons Shelters in Dikwa, Nigeria
version: null
vulnerability: null
---
