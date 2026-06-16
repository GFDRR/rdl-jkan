---
attributions:
- entity:
    affiliation: null
    email: null
    name: UNOSAT
    url: https://data.humdata.org/dataset/geodata-of-domiz-refugee-camp-duhok-governorate-iraq-january-10-2014
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-domiz-refugee-camp-duhok-governorate-iraq-january-10-2014
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-domiz-refugee-camp-duhok-governorate-iraq-january-10-2014
dataset_id: rdls_exp-irqsyr_unosat_geodatadomizrefugeecampdu_20140110
description: 'This map illustrates satellite-detected shelters and other buildings
  at the Domiz refugee camp in Duhok Governorate, Iraq. As of 25 December 2013 a total
  of 9,367 standard shelters were detected, 990 improvised structures likely being
  used for shelter and other purposes, and 592 infrastructure and support buildings.
  Domiz refugee camp is encircled by a fence that surrounds the perimeter of the camp
  and delineates the 149.76 hectares of the camp area. Areas that were in preparation
  of the ground for new construction as 21 July 2013, as 25 December 2013 contain
  a total of 584 new shelters (estimated). New expansion areas are also visible in
  the image as of 25 December 2013, indicating preparations are underway to accommodate
  increased numbers of refugees in the near future. This is a preliminary analysis
  and has not yet been validated in the field; structure locations subject to a spatial
  error margin of +/- three meters. Please send ground feedback to UNITAR/UNOSAT..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-domiz-refugee-camp-duhok-governorate-iraq-january-10-2014]'
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
    description: Satellite-detected shelters and buildings at Domiz refugee camp,
      classified by type (standard shelters, improvised structures, infrastructure/support
      buildings)
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
    description: Refugee population shelter inventory at Domiz camp, Duhok Governorate,
      Iraq, as of December 2013
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
  description: Satellite imagery was analyzed by UNOSAT analysts to detect and classify
    shelters and buildings at Domiz refugee camp in Duhok Governorate, Iraq, as of
    25 December 2013. Analysts compared multi-temporal imagery to identify standard
    shelters, improvised structures, and infrastructure buildings, and to delineate
    the camp perimeter and areas under new construction. The resulting geodata provides
    a spatial inventory of the refugee camp's built environment for humanitarian planning
    and disaster risk assessment.
  sources:
  - id: source_1
    license: null
    name: UNOSAT
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/geodata-of-domiz-refugee-camp-duhok-governorate-iraq-january-10-2014
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
  description: Geodata of Domiz Refugee Camp, Duhok Governorate, Iraq (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SY/CE20130604SYR/Domiz_20131225_SHP.zip
  format: null
  id: resource_f0863bde
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Domiz_20131225_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Domiz Refugee Camp, Duhok Governorate, Iraq (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SY/CE20130604SYR/Domiz_20131225.gdb.zip
  format: null
  id: resource_7f06cf62
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Domiz_20131225.gdb.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-irqsyr_unosat_geodatadomizrefugeecampdu_20140110
spatial:
  bbox: null
  centroid: null
  countries:
  - SYR
  - IRQ
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2014-01-10'
temporal_resolution: null
title: Geodata of Domiz Refugee Camp, Duhok Governorate, Iraq
version: null
vulnerability: null
---
