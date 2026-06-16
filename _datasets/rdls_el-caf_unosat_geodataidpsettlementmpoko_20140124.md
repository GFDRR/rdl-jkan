---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-idp-settlement-m-poko-airport-bangui-central-african-republic-january-24-2014
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-idp-settlement-m-poko-airport-bangui-central-african-republic-january-24-2014
dataset_id: rdls_el-caf_unosat_geodataidpsettlementmpoko_20140124
description: 'This map illustrates satellite-detected areas of IDP shelters in M Poko
  Airport in Bangui, Central African Republic. Using satellite images acquired on
  the 28 December 2013 by the QuickBird satellite, UNOSAT reviewed the airport grounds
  and delineated 22.3 ha of area where IDPs are living in shelters and in the open.
  Imagery acquired on 20 January 2014 shows that the IDP camp extent has increased
  compared with the previous UNOSAT analysis. The total area of IDPs occupies 26.8
  ha as of 20 January 2014, although imagery shows areas where terrain has been cleared
  and shelters have been relocated. Note that IDP occupied areas include improvised
  shelters and, in some cases, administrative support and other structures. An area
  of expansion is also visible in the image as of 20 January 2014, indicating preparations
  are underway to accommodate increased numbers of refugees in the near future. This
  is a preliminary analysis and has not yet been validated in the field. Please send
  ground feedback to UNITAR / UNOSAT.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-idp-settlement-m-poko-airport-bangui-central-african-republic-january-24-2014]'
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
    description: Internally displaced persons (IDPs) living in shelters at M Poko
      Airport settlement
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
license: CC-BY-4.0
lineage:
  description: UNOSAT analysts reviewed QuickBird satellite imagery acquired on 28
    December 2013 and 20 January 2014, comparing multi-temporal images to delineate
    IDP shelter areas and quantify settlement extent (22.3 ha and 26.8 ha respectively).
    Spatial polygons were digitized from satellite-detected shelter clusters to create
    a geodatabase of displaced population locations in the M Poko Airport settlement.
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
- href: https://data.humdata.org/dataset/geodata-of-idp-settlement-m-poko-airport-bangui-central-african-republic-january-24-2014
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Displaced population from complex emergency/conflict residing in
      IDP settlement
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: displaced
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
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
  description: Geodata of IDP Settlement, M Poko Airport, Bangui, Central African
    Republic (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/CF/CE20131212CAF/CE20131212CAF_shp.zip
  format: null
  id: resource_88b94726
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20131212CAF_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of IDP Settlement, M Poko Airport, Bangui, Central African
    Republic (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/CF/CE20131212CAF/CE20131212CAF.gdb.zip
  format: null
  id: resource_0cb07682
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20131212CAF.gdb.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-caf_unosat_geodataidpsettlementmpoko_20140124
spatial:
  bbox: null
  centroid: null
  countries:
  - CAF
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2014-01-24'
temporal_resolution: null
title: Geodata of IDP Settlement, M Poko Airport, Bangui, Central African Republic
version: null
vulnerability: null
---
