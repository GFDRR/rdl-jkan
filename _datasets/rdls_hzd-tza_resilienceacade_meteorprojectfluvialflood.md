---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: motimb@utu.fi
  name: Monica Timbuka
  url: https://crd.resilienceacademy.ac.tz/api/v2/users/1550
creator:
  affiliation: null
  email: motimb@utu.fi
  name: Monica Timbuka
  url: https://crd.resilienceacademy.ac.tz/api/v2/users/1550
dataset_id: rdls_hzd-tza_resilienceacade_meteorprojectfluvialflood
description: 'The data presented here show the modelled water depth for flood events
  of different return periods. Both fluvial flooding (flooding from rivers) and pluvial
  flooding (local surface water flooding from extreme rainfall) have been simulated
  and can be displayed. Depths are shown in meters. Note that one would not expect
  all the displayed flooding to happen at the same time; rather, the data show the
  maximum water depth that would be expected if a flood event of the specified return
  period were occurring at that location. Another way of expressing this is to say
  that the data show the probability of experiencing a given water depth within a
  single year; i.e. depths shown by the ''1-in-100 year'' layer have a 1-in-100 (or
  1%) chance of occurrence in any given year. For more information about the METEOR
  project, please see http://meteor-project.org/. If you find data useful, please
  provide feedback via our questionnaire, it should take only a few minutes: https://forms.gle/DQjhE89CRegNKB3X8.
  [Source: This metadata record was automatically extracted from the GeoNode portal
  resilienceacademy]'
details: EPSG:4326 - WGS 84 - Geographic.
exposure: []
hazard:
  event_sets:
  - analysis_type: probabilistic
    calculation_method: simulated
    event_count: 2
    events:
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_flood
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_100yr
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.01
          probability: null
          return_period: 100
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_flood
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_200yr
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.005
          probability: null
          return_period: 200
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://opendatacommons.org/licenses/odbl/1-0/
lineage:
  description: 'The data has been produced using the Fathom global flood hazard modelling
    framework (a development of Sampson et al., 2015 and Smith et al., 2015). The
    model uses the MERIT global DEM and hydrography for elevation and river network
    data sources respectively (Yamazaki et al., 2017; Yamazaki et al., 2019). The
    framework automatically constructs flood models across a specified region, using
    the two-dimensional shallow water equations to simulate the behavior of floodwaters
    during the modelled flood events. The framework produces maps of flood depths
    at 3 arcsecond (~90m) spatial resolution for a specified range of return periods.
    For a detailed technical description of the methods, please see the open-access
    academic papers listed below. Given that the modelling framework used to create
    this data is semi-autonomous and uses data available at the regional to global
    scale, its accuracy is limited by the quality of this input data and the simplified
    range of processes it can represent. While the data is suitable for providing
    guidance at the regional scale, it is not recommended to use the data for detailed
    local scale assessments or engineering purposes. More details around appropriate
    use can be found in the user training documentation (link here). Open access journal
    hyperlinks: Sampson et al 2015 https://doi.org/10.1002/2015WR016954 Smith et al
    2015: https://doi.org/10.1002/2014WR015814 Yamazaki et al 2017: https://doi.org/10.1002/2017GL072874
    Yamazaki et al 2019: https://doi.org/10.1029/2019WR024873.'
  sources:
  - id: source_1
    license: null
    name: Monica Timbuka
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://crd.resilienceacademy.ac.tz/catalogue/#/dataset/700
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Msilikale Msilanga
  url: https://geonode.resilienceacademy.ac.tz
purpose: Risk awareness and risk mitigation.
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: METEOR Project Fluvial Flood Hazard Map for Tanzania (Defended_ 1 in
    200 years)
  download_url: https://crd.resilienceacademy.ac.tz/api/v2/assets/100/link
  format: null
  id: resource_0
  media_type: image/tiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: fd_1in200_c502335cba0d5b2aba72a4c2ff92aece
- access_url: https://geonode.resilienceacademy.ac.tz/datasets/geonode:geonode:fd_1in200_c502335cba0d5b2aba72a4c2ff92aece
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wms
  coordinate_system: EPSG:4326
  description: 'METEOR Project Fluvial Flood Hazard Map for Tanzania (Defended_ 1
    in 200 years) (OGC WMS: geonode Service)'
  download_url: https://crd.resilienceacademy.ac.tz/geoserver/ows?service=WMS&version=1.1.1&request=GetMap&layers=geonode:geonode:fd_1in200_c502335cba0d5b2aba72a4c2ff92aece&format=image%2Fpng
  format: null
  id: resource_1
  media_type: image/png
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WMS: geonode Service'
- access_url: https://geonode.resilienceacademy.ac.tz/datasets/geonode:geonode:fd_1in200_c502335cba0d5b2aba72a4c2ff92aece
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wcs
  coordinate_system: EPSG:4326
  description: 'METEOR Project Fluvial Flood Hazard Map for Tanzania (Defended_ 1
    in 200 years) (OGC WCS: geonode Service)'
  download_url: https://crd.resilienceacademy.ac.tz/geoserver/ows?service=WCS&version=2.0.1&request=DescribeCoverage&CoverageId=geonode__geonode:fd_1in200_c502335cba0d5b2aba72a4c2ff92aece
  format: null
  id: resource_2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WCS: geonode Service'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: METEOR Project Fluvial Flood Hazard Map for Tanzania (Defended_ 1 in
    200 years)
  download_url: https://crd.resilienceacademy.ac.tz/geoserver/ows?service=WCS&request=GetCoverage&coverageid=geonode__fd_1in200_c502335cba0d5b2aba72a4c2ff92aece&format=image%2Ftiff&version=2.0.1&compression=DEFLATE&tileWidth=512&tileHeight=512
  format: null
  id: resource_3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GeoTIFF
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-tza_resilienceacade_meteorprojectfluvialflood
spatial:
  bbox:
  - 29.275000000001
  - -12.608333332899669
  - 40.94166666666767
  - -0.941666666233001
  centroid: null
  countries:
  - TZA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: 2019
  duration: null
  end: null
  start: null
temporal_resolution: null
title: METEOR Project Fluvial Flood Hazard Map for Tanzania (Defended_ 1 in 200 years)
version: '2019'
vulnerability: null
---
