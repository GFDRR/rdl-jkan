---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-idp-shelter-changes-in-baidoa-somalia-between-08-february-and-02-o-october-31-2014
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-idp-shelter-changes-in-baidoa-somalia-between-08-february-and-02-o-october-31-2014
dataset_id: rdls_el-som_unosat_geodataidpshelterchangesb_20141031
description: 'This map illustrates areas of IDP shelter changes within the area of
  Baidoa, Somalia occurring between 8 February and 2 October 2014, and as seen by
  the Pleiades and WorldView-3 satellites. UNOSAT analysis 25 new IDP and 14 expanded
  IDP settlement areas by 2 October 2014. However, 18 other settlement areas contracted
  and 5 areas were no longer visible, and so the overall number of structures did
  not change significantly. Specifically, the number of structures increased from
  7,910 on 8 February 2014 to 7,990 on 2 October 2014. The 90 IDP areas visible on
  2 October 2014 occupy an area of approximatively 40.3 ha, which represent an increase
  of 1.54 ha since the previous analysis 8 February 2014. This is a preliminary analysis
  and has not yet been validated in the field. Please send ground feedback to UNITAR
  / UNOSAT.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-idp-shelter-changes-in-baidoa-somalia-between-08-february-and-02-o-october-31-2014]'
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
    description: IDP shelter structures identified and tracked through satellite imagery
      analysis
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
  description: UNOSAT analysts compared multi-temporal satellite imagery (Pleiades
    and WorldView-3) acquired on 8 February 2014 and 2 October 2014 to identify and
    map changes in IDP shelter settlements in Baidoa, Somalia. Visual interpretation
    detected 25 new settlements, 14 expanded settlements, 18 contracted settlements,
    and 5 disappeared settlements, with structure counts tracked to quantify displacement
    dynamics in a complex emergency context.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/geodata-of-idp-shelter-changes-in-baidoa-somalia-between-08-february-and-02-o-october-31-2014
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: IDP shelter changes (new, expanded, contracted, disappeared) reflecting
      population displacement dynamics
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
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
  description: Geodata of IDP Shelter changes in Baidoa, Somalia, Between 08 February
    and 02 October 2014 (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SO/CE20130710SOM/CE20130710SOM_shp.zip
  format: null
  id: resource_108dcf27
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20130710SOM_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of IDP Shelter changes in Baidoa, Somalia, Between 08 February
    and 02 October 2014 (Shapefile)
  download_url: https://cern.ch/unosat-maps/SO/CE20130710SOM/CE20130710SOM.gdb.zip
  format: null
  id: resource_1e40d946
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20130710SOM.gdb.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-som_unosat_geodataidpshelterchangesb_20141031
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
  start: '2014-10-31'
temporal_resolution: null
title: Geodata of IDP Shelter changes in Baidoa, Somalia, Between 08 February and
  02 October 2014
version: null
vulnerability: null
---
