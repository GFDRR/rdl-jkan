---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Earth and Oceans Observations Team Pacific Community
  url: https://geonode.pacificdata.org/catalogue/#/dataset/574
creator:
  affiliation: null
  email: null
  name: Earth and Oceans Observations Team Pacific Community
  url: https://geonode.pacificdata.org/catalogue/#/dataset/574
dataset_id: rdls_hzd-mhl_pacificdata_coastalfloodmapsmarshalli
description: 'Coastal flood models for the Republic of Marshall Islands, showing flood
  depth in meters, for ARI100 (Average Recurrence Interval of 100 years, i.e. of a
  flood of such magnitude that it is projected to occur or be exceeded every 100 years),
  with 1.5 m Sea Level Rise (SLR). The flood models are modelled based on a modified
  5m DEM created by NIWA and SPC as part of the PARTneR 2 project, available on Nexus.
  Currently, only ARI100 with 0m, 0.5m, 1m, and 1.5m SLR is available on Nexus for
  Cook Islands, Republic of Marshall Islands, Samoa, Tonga, Tuvalu and Vanuatu. However,
  for all 6 countries, the models available are MHWS, ARI5, ARI10, ARI50, ARI100,
  ARI250 for 0 to 2m SLR in 0.1m increments. Please contact the NIWA or SPC contact
  for more information or access to these extra models. These models were created
  using a bathtub modelling approach, so may have limited accuracy and for smaller
  areas of interest, hydrodynamic models should be used for decision making. [Source:
  This metadata record was automatically extracted from the GeoNode portal pacificdata]'
details: The modified 5m DEMs, completed as part of the PARTneR 2 project, can be
  found on Nexus. The DEM was created from a mixture of upsampled 30m FABDEM V1-0
  (Forest and Building removed Copernicus DEM), FABDEM V1-2 and downsampled 1m LiDAR-derived
  DEM where this data was available. SPC undertook the rapid coastal inundation assessment
  based on the first available TC vitals after cyclone landfall. Storm surges and
  waves are simulated with the ADCIRC+SWAN coupled wave circulation model (Dietrich
  et al., 2011), running in a non-structured mesh. Atmospheric forcings (i.e., surface
  pressure and winds) are generated with the parametric Dynamic Holland Model (Flemming
  et al., 2007), and tidal forcing along the boundaries comes from TPXO8 (Egbert and
  Erofeeva, 2002). Nearshore waves are transformed to the 2% exceedance water level
  based on the empirical relation of Merrifield et al., 2014, which is linearly added
  to the storm tide levels resolved by the model to account for the wave contribution
  to the Total Water Level. The TWL along each island is then approximated to a 2D
  surface that intersects the 5 m DEM to produce the inundation maps.
exposure: []
hazard:
  event_sets:
  - analysis_type: probabilistic
    calculation_method: simulated
    event_count: 1
    events:
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_flood
        intensity_measure: wd:m
        process: coastal_flood
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
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: wd:m
      process: coastal_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: flood
license: CC-BY-4.0
lineage:
  description: The coastal flood map rasters were created based on a modified 5m DEM
    created by NIWA and SPC as part of the PARTneR 2 project, based on the FABDEM
    and LiDAR data where available, and a rapid coastal inundation hazard assessment.
    These models were created using a bathtub modelling approach, so may have limited
    accuracy and for smaller areas of interest, hydrodynamic models should be used
    for decision making.
  sources:
  - id: source_1
    license: null
    name: Earth and Oceans Observations Team Pacific Community
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://geonode.pacificdata.org/catalogue/#/dataset/574
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Earth and Oceans Observations Team Pacific Community
  url: https://geonode.pacificdata.org
purpose: The dataset was developed as part of the PARTneR 2 project, funded by the
  New Zealand Ministry of Foreign Affairs and Trade (MFAT) and was jointly delivered
  by the Pacific Community (SPC) and NIWA, in collaboration with the partner countries.
  It aimed to help countries in the Pacific become more resilient to the impacts of
  climate-related hazards, while building on the pilot PARTneR project, which ran
  from 2016-2019. The project activities included co-developing national risk models
  and assessment tools. The coastal flood bathtub models were developed for Tonga,
  Samoa, Cook Islands, Republic of Marshall Islands, Vanuatu and Tuvalu, based on
  requests from in-country consultations.
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Coastal flood maps, Marshall Islands, ARI100, SLR 1.5
  download_url: https://geonode.pacificdata.org/geoserver/ows?service=WCS&request=GetCoverage&coverageid=geonode__mh_coastalfloodmap_ari100_s15&format=image%2Ftiff&version=2.0.1&compression=DEFLATE&tileWidth=512&tileHeight=512
  format: null
  id: resource_0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GeoTIFF
- access_url: https://geonode.pacificdata.org/datasets/geonode:mh_coastalfloodmap_ari100_s15
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wms
  coordinate_system: EPSG:4326
  description: 'Coastal flood maps, Marshall Islands, ARI100, SLR 1.5 (OGC WMS: geonode
    Service)'
  download_url: https://geonode.pacificdata.org/geoserver/ows?service=WMS&version=1.1.1&request=GetMap&layers=geonode:mh_coastalfloodmap_ari100_s15&format=image%2Fpng
  format: null
  id: resource_1
  media_type: image/png
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WMS: geonode Service'
- access_url: https://geonode.pacificdata.org/datasets/geonode:mh_coastalfloodmap_ari100_s15
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wcs
  coordinate_system: EPSG:4326
  description: 'Coastal flood maps, Marshall Islands, ARI100, SLR 1.5 (OGC WCS: geonode
    Service)'
  download_url: https://geonode.pacificdata.org/geoserver/ows?service=WCS&version=2.0.1&request=DescribeCoverage&CoverageId=geonode__mh_coastalfloodmap_ari100_s15
  format: null
  id: resource_2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WCS: geonode Service'
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-mhl_pacificdata_coastalfloodmapsmarshalli
spatial:
  bbox:
  - 162.03382063728858
  - 4.569769624594495
  - 172.17544844529715
  - 12.289988889030745
  centroid: null
  countries:
  - MHL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: 2024
  duration: null
  end: null
  start: null
temporal_resolution: null
title: Coastal flood maps, Marshall Islands, ARI100, SLR 1.5
version: null
vulnerability: null
---
