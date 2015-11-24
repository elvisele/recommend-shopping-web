package MahoutTest.Test01;

import java.io.File;
import java.util.ArrayList;
import java.util.List;

import org.apache.mahout.cf.taste.impl.model.file.FileDataModel;
import org.apache.mahout.cf.taste.impl.recommender.GenericItemBasedRecommender;
import org.apache.mahout.cf.taste.impl.similarity.LogLikelihoodSimilarity;
import org.apache.mahout.cf.taste.model.DataModel;
import org.apache.mahout.cf.taste.recommender.ItemBasedRecommender;
import org.apache.mahout.cf.taste.recommender.RecommendedItem;
import org.apache.mahout.cf.taste.similarity.ItemSimilarity;

import py4j.GatewayServer;

public class javarecomend {
	
public ItemBasedRecommender prepdata() throws Exception{
	DataModel model = new FileDataModel(new File("dataset/ratings_itemID_exit_Bookinfo.txt"));
	ItemSimilarity similarity = new LogLikelihoodSimilarity(model);
	ItemBasedRecommender recommender = new GenericItemBasedRecommender(model, similarity);
	return recommender;
}

public List<Long> itemrecommend(Long itemid,ItemBasedRecommender recommender) throws Exception{
	List<RecommendedItem> recommendations = recommender.mostSimilarItems(itemid, 10);
	List<Long> item = new ArrayList<Long>();
	for (RecommendedItem recommendation : recommendations) {
		item.add(recommendation.getItemID());
	}
	return item;
}

	public static void main(String[] args) throws Exception {
		javarecomend app = new javarecomend();
	    GatewayServer server = new GatewayServer(app);
	    server.start();
	    System.out.println("server start");
	}

}
