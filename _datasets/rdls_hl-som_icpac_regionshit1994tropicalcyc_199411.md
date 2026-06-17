---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: IGAD Climate Prediction and Applications Center (ICPAC)
  url: https://data.humdata.org/dataset/icpac-geonode-somalia-regions-hit-by-1994-tropical-cyclone-05a
creator:
  affiliation: null
  email: null
  name: IGAD Climate Prediction and Applications Center (ICPAC)
  url: https://data.humdata.org/dataset/icpac-geonode-somalia-regions-hit-by-1994-tropical-cyclone-05a
dataset_id: rdls_hl-som_icpac_regionshit1994tropicalcyc_199411
description: 'In November 20, 1994 TC05A moved ashore eastern Somalia near Eyl district,
  producing wind speeds of 104 km/h (65 mph) in Bosaso district. This layer shows
  the occurence of the storm in two regions of Somalia; Bari and Nugaal Province.
  The disturbance which became TC05A was first noted on 7 November,1994 by Significant
  Tropical Weather Advisory (ABIO) at 9N 54E. It was embedded within a widespread
  area of convection associated with broad troughing. The first warning was issued
  at 0600Z on 8 November as the cyclone landed in Somalia. The storm''s high winds
  and rainfall killed 30 people and injured hundreds of others. Several boats and
  homes were washed away.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/icpac-geonode-somalia-regions-hit-by-1994-tropical-cyclone-05a]'
details: null
exposure: []
hazard:
  event_sets:
  - analysis_type: probabilistic
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: sws_10m:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: strong_wind
license: CC-BY-4.0
lineage:
  description: Post-event observational data from ICPAC documenting the track, intensity,
    and spatial extent of tropical cyclone TC05A as it made landfall in eastern Somalia
    on November 20, 1994, with recorded wind speeds and associated mortality impacts
    in Bari and Nugaal provinces.
  sources:
  - id: source_1
    license: null
    name: IGAD Climate Prediction and Applications Center (ICPAC)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/icpac-geonode-somalia-regions-hit-by-1994-tropical-cyclone-05a
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Direct fatalities from tropical cyclone TC05A in Somalia regions
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: casualty_count
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: probabilistic
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
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__1994_TC_05A&outputFormat=csv&srs=EPSG%3A4326
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: CSV file. In November 20, 1994 TC05A moved ashore eastern Somalia near
    Eyl district, producing wind speeds of 104 km/h (65 mph) in Bosaso district. This
    layer shows the occurence of the storm in two regions of Somalia; Bari and Nugaal
    Province.
  download_url: null
  format: null
  id: resource_9189c107
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Somalia Regions hit by 1994 Tropical Cyclone 05A CSV
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__1994_TC_05A&outputFormat=excel&srs=EPSG%3A4326
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: Excel file. In November 20, 1994 TC05A moved ashore eastern Somalia
    near Eyl district, producing wind speeds of 104 km/h (65 mph) in Bosaso district.
    This layer shows the occurence of the storm in two regions of Somalia; Bari and
    Nugaal Province.
  download_url: null
  format: null
  id: resource_61a64863
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Somalia Regions hit by 1994 Tropical Cyclone 05A Excel
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__1994_TC_05A&outputFormat=json&srs=EPSG%3A4326&srsName=EPSG%3A4326
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: GeoJSON file. In November 20, 1994 TC05A moved ashore eastern Somalia
    near Eyl district, producing wind speeds of 104 km/h (65 mph) in Bosaso district.
    This layer shows the occurence of the storm in two regions of Somalia; Bari and
    Nugaal Province.
  download_url: null
  format: null
  id: resource_30d3653c
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Somalia Regions hit by 1994 Tropical Cyclone 05A GeoJSON
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__1994_TC_05A&outputFormat=SHAPE-ZIP&srs=EPSG%3A4326&format_options=charset%3AUTF-8
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: Zipped Shapefile file. In November 20, 1994 TC05A moved ashore eastern
    Somalia near Eyl district, producing wind speeds of 104 km/h (65 mph) in Bosaso
    district. This layer shows the occurence of the storm in two regions of Somalia;
    Bari and Nugaal Province.
  download_url: null
  format: null
  id: resource_69182235
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Somalia Regions hit by 1994 Tropical Cyclone 05A Zipped Shapefile
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-som_icpac_regionshit1994tropicalcyc_199411
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
  end: '1994-11-20'
  start: '1994-11-19'
temporal_resolution: null
title: Somalia Regions hit by 1994 Tropical Cyclone 05A
version: null
vulnerability: null
---
