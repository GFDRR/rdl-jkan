---
attributions:
- entity:
    affiliation: null
    email: null
    name: UNOSAT
    url: https://data.humdata.org/dataset/geodata-of-damage-assesment-in-bangui-central-african-republic-july-02-2014
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assesment-in-bangui-central-african-republic-july-02-2014
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assesment-in-bangui-central-african-republic-july-02-2014
dataset_id: rdls_lss-caf_unosat_geodatadamageassesmentban_20140702
description: 'This map illustrates locations of destroyed structures within the arrondissements
  of Bangui, Central African Republic. Using satellite imagery acquired 16 November
  2013, 22 February 2014, and 6 June 2014 UNOSAT reviewed the city of Bangui to locate
  signs of destroyed structures. By 22 February 2014, a total of 1,872 structures
  were destroyed in the area of Bangui, with 1,341 structures detected in the 8 arrondissements
  and an additional 531 located in the surrounding area. As of 6 June 2014 a total
  of 368 damaged structures have been reconstructed and 871 additional structures
  have been severely damaged or destroyed since 22 February 2014. Pre-crisis imagery
  used for this analysis was collected on 16 November 2013, and thus structures destroyed
  previous to 16 November 2013 are not indicated on this map. This is a preliminary
  analysis & has not yet been validated in the field. Please send ground feedback
  to UNITAR / UNOSAT.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-damage-assesment-in-bangui-central-african-republic-july-02-2014]'
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: UNOSAT analysts conducted multi-temporal satellite imagery analysis
    comparing images from November 2013, February 2014, and June 2014 to identify
    and geolocate destroyed structures in Bangui. The assessment tracked both initial
    destruction (1,872 structures) and subsequent reconstruction (368 structures)
    across the city's arrondissements.
  sources:
  - id: source_1
    license: null
    name: UNOSAT
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/geodata-of-damage-assesment-in-bangui-central-african-republic-july-02-2014
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Destroyed and reconstructed structures identified through satellite
      imagery analysis during conflict-related violence in Bangui
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
        metric: loss
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
  description: Geodata of Damage Assesment in Bangui, Central African Republic (Shapefile)
  download_url: https://cern.ch/unosat-maps/CF/CE20131212CAF/CE20131212CAF_shp.zip
  format: null
  id: resource_668d3ae2
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
  description: Geodata of Damage Assesment in Bangui, Central African Republic (Shapefile)
  download_url: https://cern.ch/unosat-maps/CF/CE20131212CAF/CE20131212CAF.gdb.zip
  format: null
  id: resource_dec63262
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20131212CAF.gdb.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-caf_unosat_geodatadamageassesmentban_20140702
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
  start: '2014-07-02'
temporal_resolution: null
title: Geodata of Damage Assesment in Bangui, Central African Republic
version: null
vulnerability: null
---
