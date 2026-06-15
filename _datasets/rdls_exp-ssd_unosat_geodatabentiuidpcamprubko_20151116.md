---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-bentiu-idp-camp-rubkona-county-unity-state-south-sudan-november-16-2015
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-bentiu-idp-camp-rubkona-county-unity-state-south-sudan-november-16-2015
dataset_id: rdls_exp-ssd_unosat_geodatabentiuidpcamprubko_20151116
description: 'This map illustrates satellite-detected shelters and other buildings
  in the Bentiu UNMISS base as seen by the WorldView-2 satellite on 31 October 2015.
  Imagery collected on this date shows that the IDPs within the base Protection of
  Civilian (PoCs) areas has increased by more than 12% since the previous UNOSAT analysis,
  done using an image collected 7 March 2015. As of 31 October 2015, a total of 12,641
  shelters were detected within the PoCs and Contingency zones, but excluding structures
  within the UNMISS base boundary. Specifically, 10,925 structures were tent shelters
  and 1,685 were camp infrastructure buildings. The remaining 31 structures where
  found outside the delineated areas and consisted mainly of sentry posts and watch
  towers. This is a preliminary analysis & has not yet been validated in the field.
  Please send ground feedback to UNITAR -UNOSAT.. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/geodata-of-bentiu-idp-camp-rubkona-county-unity-state-south-sudan-november-16-2015]'
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
    description: Satellite-detected shelter and building structures in Bentiu IDP
      camp, classified by type (tent vs. permanent structures)
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
  description: UNOSAT analysts manually reviewed and analyzed WorldView-2 satellite
    imagery acquired on 31 October 2015, comparing it with prior imagery from 7 March
    2015 to detect changes in shelter distribution and count structures within the
    Bentiu IDP camp. Shelters were classified by type (tent vs. permanent) and spatially
    mapped as point or polygon features with confidence and validation metadata.
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
- href: https://data.humdata.org/dataset/geodata-of-bentiu-idp-camp-rubkona-county-unity-state-south-sudan-november-16-2015
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
  description: Geodata of Bentiu IDP Camp, Rubkona County, Unity State, South Sudan
    (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SS/CE20131218SSD/CE20131218SSD_shp.zip
  format: null
  id: resource_a54e3e5c
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20131218SSD_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Bentiu IDP Camp, Rubkona County, Unity State, South Sudan
    (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SS/CE20131218SSD/CE20131218SSD.gdb.zip
  format: null
  id: resource_4c659a0f
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20131218SSD.gdb.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-ssd_unosat_geodatabentiuidpcamprubko_20151116
spatial:
  bbox: null
  centroid: null
  countries:
  - SSD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-11-16'
temporal_resolution: null
title: Geodata of Bentiu IDP Camp, Rubkona County, Unity State, South Sudan
version: null
vulnerability: null
---
