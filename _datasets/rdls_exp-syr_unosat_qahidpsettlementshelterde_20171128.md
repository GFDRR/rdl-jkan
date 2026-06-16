---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/qah-idp-settlement-shelter-density-in-dana-subdistrict-harem-district-idlib-governorate-syria-2743
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/qah-idp-settlement-shelter-density-in-dana-subdistrict-harem-district-idlib-governorate-syria-2743
dataset_id: rdls_exp-syr_unosat_qahidpsettlementshelterde_20171128
description: 'This map illustrates density of satellite-detected shelters and other
  buildings at the Qah Internally Displaced Persons settlement in Dana Subdistrict,
  Harem District, Idlib Governorate, Syria. As of 12 July 2017, a total of 18,547
  shelters were detected as well as 333 infrastructure and support buildings within
  the displayed area. This represents an increase in structures of over 73% since
  the previous UNOSAT analysis using an image from 22 May 2015, when the number of
  shelters was 10,898 and the number of infrastructure and support buildings was 48
  within the same area.The full UNOSAT analysis detected 45,591 structures over the
  Dana Subdistrict as of 12 July 2017. This is a preliminary analysis and has not
  yet been validated in the field. Please send ground feedback to UNITAR-UNOSAT..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/qah-idp-settlement-shelter-density-in-dana-subdistrict-harem-district-idlib-governorate-syria-2743]'
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
    description: Satellite-detected shelter and infrastructure buildings in IDP settlement,
      classified by structure type and temporal change
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
  description: UNOSAT analysts reviewed and compared satellite imagery from 12 July
    2017 against a baseline image from 22 May 2015 to detect and map shelter and infrastructure
    buildings in the Qah IDP settlement. Building structures were identified through
    visual interpretation of satellite imagery and classified by type (shelter vs.
    infrastructure/support). The dataset provides a spatial inventory of structures
    with confidence levels and temporal trend analysis showing 73% increase in structures
    over the 26-month period.
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
- href: https://data.humdata.org/dataset/qah-idp-settlement-shelter-density-in-dana-subdistrict-harem-district-idlib-governorate-syria-2743
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
  description: Qah IDP settlement shelter density in Dana Subdistrict, Harem District,
    Idlib Governorate, Syria (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SY/CE20130604SYR/UNOSAT_IDP_SYR_20170712.gdb.zip
  format: Geodatabase
  id: resource_f604a94a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_IDP_SYR_20170712.gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Qah IDP settlement shelter density in Dana Subdistrict, Harem District,
    Idlib Governorate, Syria (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SY/CE20130604SYR/UNOSAT_IDP_SYR_20170712_shp.zip
  format: null
  id: resource_874693e7
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_IDP_SYR_20170712_shp.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-syr_unosat_qahidpsettlementshelterde_20171128
spatial:
  bbox: null
  centroid: null
  countries:
  - SYR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-11-28'
temporal_resolution: null
title: Qah IDP settlement shelter density in Dana Subdistrict, Harem District, Idlib
  Governorate, Syria
version: null
vulnerability: null
---
