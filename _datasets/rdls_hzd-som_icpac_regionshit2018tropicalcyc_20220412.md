---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: IGAD Climate Prediction and Applications Center (ICPAC)
  url: https://data.humdata.org/dataset/icpac-geonode-somalia-regions-hit-by-2018-tropical-cyclone-sagar
creator:
  affiliation: null
  email: null
  name: IGAD Climate Prediction and Applications Center (ICPAC)
  url: https://data.humdata.org/dataset/icpac-geonode-somalia-regions-hit-by-2018-tropical-cyclone-sagar
dataset_id: rdls_hzd-som_icpac_regionshit2018tropicalcyc_20220412
description: 'Global Disaster Alert and Coordination System described Cyclone Sagar
  as one of the strongest storms ever recorded in Somalia. This was a very rare cyclone
  in the Gulf of Aden that made landfall in north-western Somaliland on 19 May, 2018.
  This layer shows the occurence of TC Sagar in some regions of Somalia,including
  Awdal, Togdheer, Sool, Sanaag, Bari, Hiraan, Gedo and Lower Juba.The TC Sagar moved
  with wind gusts of up to 120 km/hour that delivered a year&rsquo;s worth of rain
  to some areas in the north, that is between 150 and 200mm. TC Sagar was reported
  to have adverse impacts on Somalia regions. The United Nations Office for the Coordination
  of Humanitarian Affairs (OCHA) reported heavy rainfall, strong winds and dangerous
  flash floods hitting coastal areas of Puntland and Somaliland. This resulted in
  the loss of lives, crops and livestock as well as the destruction of property and
  infrastructure. Recored impacts according to regions included: Awdal, Bari, Sanaag,
  Sool, Togdheer Number of people affected: 228,000 Number of people displaced: 9,000
  Awdal, Hiraan, Gedo, Lower Juba Number of people affected:830,000 Number of people
  worst hit:170,000 Number of people displaced: 290,000 Number of people death: 50
  Infrusructure destroyed:(20-40)schools and 21 health facilities. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/icpac-geonode-somalia-regions-hit-by-2018-tropical-cyclone-sagar]'
details: Time period is set to publication date rather than the date the data covers
exposure: []
hazard:
  event_sets_by_hazard_type:
    strong_wind:
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
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Post-event spatial dataset documenting the geographic extent of Tropical
    Cyclone Sagar's impact across Somali administrative regions, compiled by ICPAC
    from observed meteorological data and impact reports following the May 2018 cyclone
    landfall in Somaliland.
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
- href: https://data.humdata.org/dataset/icpac-geonode-somalia-regions-hit-by-2018-tropical-cyclone-sagar
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
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2018_TC_Sagar&outputFormat=csv&srs=EPSG%3A4326
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: CSV file. Global Disaster Alert and Coordination System described Cyclone
    Sagar as one of the strongest storms ever recorded in Somalia. This was a very
    rare cyclone in the Gulf of Aden that made landfall in north-western Somaliland
    on 19 May, 2018. This layer shows the occurence of TC Sagar in some regions of
    Somalia,including Awdal, Togdheer, Sool, Sanaag, Bari, Hiraan, Gedo and Lower
    Juba.The TC Sagar moved with wind gusts of up to 120 km/hour that delivered a
    year&rsquo;s worth of rain to some areas in the north, that is between 150 and
    200mm.
  download_url: null
  format: null
  id: resource_9cdf606b
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Somalia Regions hit by 2018 Tropical Cyclone Sagar CSV
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2018_TC_Sagar&outputFormat=excel&srs=EPSG%3A4326
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: Excel file. Global Disaster Alert and Coordination System described
    Cyclone Sagar as one of the strongest storms ever recorded in Somalia. This was
    a very rare cyclone in the Gulf of Aden that made landfall in north-western Somaliland
    on 19 May, 2018. This layer shows the occurence of TC Sagar in some regions of
    Somalia,including Awdal, Togdheer, Sool, Sanaag, Bari, Hiraan, Gedo and Lower
    Juba.The TC Sagar moved with wind gusts of up to 120 km/hour that delivered a
    year&rsquo;s worth of rain to some areas in the north, that is between 150 and
    200mm.
  download_url: null
  format: null
  id: resource_c5651d43
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Somalia Regions hit by 2018 Tropical Cyclone Sagar Excel
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2018_TC_Sagar&outputFormat=json&srs=EPSG%3A4326&srsName=EPSG%3A4326
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: GeoJSON file. Global Disaster Alert and Coordination System described
    Cyclone Sagar as one of the strongest storms ever recorded in Somalia. This was
    a very rare cyclone in the Gulf of Aden that made landfall in north-western Somaliland
    on 19 May, 2018. This layer shows the occurence of TC Sagar in some regions of
    Somalia,including Awdal, Togdheer, Sool, Sanaag, Bari, Hiraan, Gedo and Lower
    Juba.The TC Sagar moved with wind gusts of up to 120 km/hour that delivered a
    year&rsquo;s worth of rain to some areas in the north, that is between 150 and
    200mm.
  download_url: null
  format: null
  id: resource_d1e84176
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Somalia Regions hit by 2018 Tropical Cyclone Sagar GeoJSON
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2018_TC_Sagar&outputFormat=SHAPE-ZIP&srs=EPSG%3A4326&format_options=charset%3AUTF-8
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: Zipped Shapefile file. Global Disaster Alert and Coordination System
    described Cyclone Sagar as one of the strongest storms ever recorded in Somalia.
    This was a very rare cyclone in the Gulf of Aden that made landfall in north-western
    Somaliland on 19 May, 2018. This layer shows the occurence of TC Sagar in some
    regions of Somalia,including Awdal, Togdheer, Sool, Sanaag, Bari, Hiraan, Gedo
    and Lower Juba.The TC Sagar moved with wind gusts of up to 120 km/hour that delivered
    a year&rsquo;s worth of rain to some areas in the north, that is between 150 and
    200mm.
  download_url: null
  format: null
  id: resource_10f8edf0
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Somalia Regions hit by 2018 Tropical Cyclone Sagar Zipped Shapefile
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-som_icpac_regionshit2018tropicalcyc_20220412
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
  start: '2022-04-12'
temporal_resolution: null
title: Somalia Regions hit by 2018 Tropical Cyclone Sagar
version: null
vulnerability: null
---
