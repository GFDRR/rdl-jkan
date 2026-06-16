---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: IGAD Climate Prediction and Applications Center (ICPAC)
  url: https://data.humdata.org/dataset/icpac-geonode-tropical-cyclones-hitting-somali-regions-for-the-period-1984-2020
creator:
  affiliation: null
  email: null
  name: IGAD Climate Prediction and Applications Center (ICPAC)
  url: https://data.humdata.org/dataset/icpac-geonode-tropical-cyclones-hitting-somali-regions-for-the-period-1984-2020
dataset_id: rdls_hzd-som_icpac_tropicalcycloneshittingre_1984
description: 'Tropical cyclones hitting Somalia Regions for the period between 1984
  to 2020. This layer indicates the frequency of cyclone occurence within specific
  regions of Somalia. The cyclones recorded include: 1984 Tropical Cyclone 1A 1984
  Tropical Cyclone 4B 1992 Tropical Cyclone 12A 1994 Tropical Cyclone 05A 1997 Tropical
  Cyclone 03A 2004 Tropical Cyclone Agni 2010 Tropical Cyclone Bandu 2012 Tropical
  Cyclone Murjan 2013 Tropical Cyclone 3A 2015 Tropical Cyclone Chapala 2015 Tropical
  Cyclone Megh 2018 Tropical Cyclone Sagar 2019 Tropical Cyclone Pawan 2020 Tropical
  Cyclone Gati. [Source: This metadata record was automatically extracted from the
  Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/icpac-geonode-tropical-cyclones-hitting-somali-regions-for-the-period-1984-2020]'
details: null
exposure: []
hazard:
  event_sets:
  - analysis_type: empirical
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
license: CC-BY-4.0
lineage:
  description: Historical tropical cyclone events affecting Somalia were compiled
    from meteorological records and aggregated by administrative region to produce
    frequency counts. The dataset represents observed cyclone occurrences over a 37-year
    period, with individual cyclone tracks and attributes stored in spatial vector
    format (shapefile, GeoJSON) and tabular format (CSV, Excel).
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
- href: https://data.humdata.org/dataset/icpac-geonode-tropical-cyclones-hitting-somali-regions-for-the-period-1984-2020
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
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3ASOM_TCmergedADMIN1_UNSOS_OCT2016_27012022&outputFormat=SHAPE-ZIP&srs=EPSG%3A4326&format_options=charset%3AUTF-8
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: 'Zipped Shapefile file. Tropical cyclones hitting Somalia Regions for
    the period between 1984 to 2020. This layer indicates the frequency of cyclone
    occurence within specific regions of Somalia. The cyclones recorded include: 1984
    Tropical Cyclone 1A 1984 Tropical Cyclone 4B 1992 Tropical Cyclone 12A 1994 Tropical
    Cyclone 05A 1997 Tropical Cyclone 03A 2004 Tropical Cyclone Agni 2010 Tropical
    Cyclone Bandu 2012 Tropical Cyclone Murjan 2013 Tropical Cyclone 3A 2015 Tropical
    Cyclone Chapala 2015 Tropical Cyclone Megh 2018 Tropical Cyclone Sagar 2019 Tropical
    Cyclone Pawan 2020 Tropical Cyclone Gati'
  download_url: null
  format: null
  id: resource_4fdb9312
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Tropical Cyclones hitting Somali Regions for the period(1984-2020) Zipped
    Shapefile
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3ASOM_TCmergedADMIN1_UNSOS_OCT2016_27012022&outputFormat=csv&srs=EPSG%3A4326
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: 'CSV file. Tropical cyclones hitting Somalia Regions for the period
    between 1984 to 2020. This layer indicates the frequency of cyclone occurence
    within specific regions of Somalia. The cyclones recorded include: 1984 Tropical
    Cyclone 1A 1984 Tropical Cyclone 4B 1992 Tropical Cyclone 12A 1994 Tropical Cyclone
    05A 1997 Tropical Cyclone 03A 2004 Tropical Cyclone Agni 2010 Tropical Cyclone
    Bandu 2012 Tropical Cyclone Murjan 2013 Tropical Cyclone 3A 2015 Tropical Cyclone
    Chapala 2015 Tropical Cyclone Megh 2018 Tropical Cyclone Sagar 2019 Tropical Cyclone
    Pawan 2020 Tropical Cyclone Gati'
  download_url: null
  format: null
  id: resource_b79a9d1c
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Tropical Cyclones hitting Somali Regions for the period(1984-2020) CSV
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3ASOM_TCmergedADMIN1_UNSOS_OCT2016_27012022&outputFormat=excel&srs=EPSG%3A4326
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: 'Excel file. Tropical cyclones hitting Somalia Regions for the period
    between 1984 to 2020. This layer indicates the frequency of cyclone occurence
    within specific regions of Somalia. The cyclones recorded include: 1984 Tropical
    Cyclone 1A 1984 Tropical Cyclone 4B 1992 Tropical Cyclone 12A 1994 Tropical Cyclone
    05A 1997 Tropical Cyclone 03A 2004 Tropical Cyclone Agni 2010 Tropical Cyclone
    Bandu 2012 Tropical Cyclone Murjan 2013 Tropical Cyclone 3A 2015 Tropical Cyclone
    Chapala 2015 Tropical Cyclone Megh 2018 Tropical Cyclone Sagar 2019 Tropical Cyclone
    Pawan 2020 Tropical Cyclone Gati'
  download_url: null
  format: null
  id: resource_ac1d650d
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Tropical Cyclones hitting Somali Regions for the period(1984-2020) Excel
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3ASOM_TCmergedADMIN1_UNSOS_OCT2016_27012022&outputFormat=json&srs=EPSG%3A4326&srsName=EPSG%3A4326
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: 'GeoJSON file. Tropical cyclones hitting Somalia Regions for the period
    between 1984 to 2020. This layer indicates the frequency of cyclone occurence
    within specific regions of Somalia. The cyclones recorded include: 1984 Tropical
    Cyclone 1A 1984 Tropical Cyclone 4B 1992 Tropical Cyclone 12A 1994 Tropical Cyclone
    05A 1997 Tropical Cyclone 03A 2004 Tropical Cyclone Agni 2010 Tropical Cyclone
    Bandu 2012 Tropical Cyclone Murjan 2013 Tropical Cyclone 3A 2015 Tropical Cyclone
    Chapala 2015 Tropical Cyclone Megh 2018 Tropical Cyclone Sagar 2019 Tropical Cyclone
    Pawan 2020 Tropical Cyclone Gati'
  download_url: null
  format: null
  id: resource_60b9aa53
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Tropical Cyclones hitting Somali Regions for the period(1984-2020) GeoJSON
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-som_icpac_tropicalcycloneshittingre_1984
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
  end: '2020-11-23'
  start: '1984-05-28'
temporal_resolution: null
title: Somalia - Tropical Cyclones hitting Somali Regions for the period(1984-2020)
version: null
vulnerability: null
---
