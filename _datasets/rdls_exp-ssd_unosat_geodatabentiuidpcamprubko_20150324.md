---
attributions:
- entity:
    affiliation: null
    email: null
    name: WorldView-3 satellite imagery
    url: https://data.humdata.org/dataset/geodata-of-bentiu-idp-camp-rubkona-county-unity-state-south-sudan-march-24-2015
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-bentiu-idp-camp-rubkona-county-unity-state-south-sudan-march-24-2015
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-bentiu-idp-camp-rubkona-county-unity-state-south-sudan-march-24-2015
dataset_id: rdls_exp-ssd_unosat_geodatabentiuidpcamprubko_20150324
description: 'This map illustrates the IDP camp at the UNMISS Protection of Civilian
  (PoC) area adjacent to the UNMISS base in Bentiu, Rubkona County, Unity State, South
  Sudan. Using high-resolution optical satellite imagery collected by the WorldView-3
  satellite on 07 March 2015, UNOSAT identified a total of 9,713 structures. Approximately
  9,515 of these were classified as tent shelters and 198 as administrative buildings.
  This is a preliminary analysis and has not yet been validated in the field. Please
  send ground feedback to UNITAR / UNOSAT.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-bentiu-idp-camp-rubkona-county-unity-state-south-sudan-march-24-2015]'
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
    description: Tent shelters and administrative buildings in Bentiu IDP camp identified
      from satellite imagery
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
    description: Internally displaced population residing in the Bentiu PoC camp
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
  description: High-resolution WorldView-3 satellite imagery from 07 March 2015 was
    analyzed by UNOSAT to identify and classify 9,713 structures within the Bentiu
    IDP camp, distinguishing between 9,515 tent shelters and 198 administrative buildings
    through manual image interpretation. The resulting geodata provides a spatial
    inventory of shelter infrastructure and population concentration in the UNMISS
    PoC area.
  sources:
  - id: source_1
    license: null
    name: WorldView-3 satellite imagery
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
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
- href: https://data.humdata.org/dataset/geodata-of-bentiu-idp-camp-rubkona-county-unity-state-south-sudan-march-24-2015
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
  download_url: https://cern.ch/unosat-maps/SS/CE20131218SSD/CE20131218SSD_Bentiu.shp.zip
  format: null
  id: resource_abe99cb2
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20131218SSD_Bentiu.shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Bentiu IDP Camp, Rubkona County, Unity State, South Sudan
    (Shapefile)
  download_url: https://cern.ch/unosat-maps/SS/CE20131218SSD/CE20131218SSD_Bentiu.gdb.zip
  format: null
  id: resource_77c67940
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20131218SSD_Bentiu.gdb.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-ssd_unosat_geodatabentiuidpcamprubko_20150324
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
  start: '2015-03-24'
temporal_resolution: null
title: Geodata of Bentiu IDP Camp, Rubkona County, Unity State, South Sudan
version: null
vulnerability: null
---
